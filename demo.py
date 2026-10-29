#!/usr/bin/env python3
"""NammaSpace DUSt3R reconstruction demo.

This is a research implementation of the DUSt3R reconstruction stage. It accepts
multiple overlapping indoor images, performs pairwise inference and global
alignment, and exports a colored point-cloud GLB for inspection in a browser or
3D viewer. The result is intentionally labelled research quality: the first
implementation produced a usable reconstruction, but its geometry was not yet
reliable enough for the full NammaSpace navigation target.
"""
from __future__ import annotations

import argparse
import os
import tempfile
from pathlib import Path

import gradio as gr
import numpy as np
import torch
import trimesh

from dust3r.cloud_opt import GlobalAlignerMode, global_aligner
from dust3r.image_pairs import make_pairs
from dust3r.inference import inference
from dust3r.model import AsymmetricCroCo3DStereo
from dust3r.utils.image import load_images

DEFAULT_MODEL = "naver/DUSt3R_ViTLarge_BaseDecoder_512_dpt"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run DUSt3R through a Gradio UI")
    parser.add_argument("--model-name", default=DEFAULT_MODEL, help="DUSt3R checkpoint or Hugging Face model id")
    parser.add_argument("--weights", default=None, help="Optional local DUSt3R checkpoint")
    parser.add_argument("--image-size", type=int, default=512, help="DUSt3R input size")
    parser.add_argument("--device", default=None, choices=["cuda", "cpu"])
    parser.add_argument("--server-name", default=None)
    parser.add_argument("--local-network", action="store_true")
    parser.add_argument("--server-port", type=int, default=7860)
    parser.add_argument("--max-images", type=int, default=12)
    parser.add_argument("--alignment-iterations", type=int, default=300)
    parser.add_argument("--output-dir", default=None)
    return parser.parse_args()


def normalize_files(files) -> list[str]:
    paths: list[str] = []
    for item in files or []:
        path = item if isinstance(item, str) else getattr(item, "name", None)
        if path and os.path.isfile(path):
            paths.append(path)
    return sorted(paths)


def _to_numpy(value):
    if torch.is_tensor(value):
        return value.detach().float().cpu().numpy()
    return np.asarray(value)


def export_scene(scene, output_path: str, confidence_percentile: float) -> str:
    points = scene.get_pts3d()
    confs = scene.get_conf()
    images = getattr(scene, "imgs", None)
    point_blocks: list[np.ndarray] = []
    color_blocks: list[np.ndarray] = []

    for index, (point_map, confidence) in enumerate(zip(points, confs)):
        xyz = _to_numpy(point_map).reshape(-1, 3)
        score = _to_numpy(confidence).reshape(-1)
        threshold = np.percentile(score, confidence_percentile)
        keep = np.isfinite(xyz).all(axis=1) & (score >= threshold)
        point_blocks.append(xyz[keep])

        if images is not None and index < len(images):
            rgb = _to_numpy(images[index])
            if rgb.ndim == 3 and rgb.shape[-1] == 3:
                rgb = (np.clip(rgb, 0, 1) * 255).astype(np.uint8)
                color_blocks.append(rgb.reshape(-1, 3)[keep])

    vertices = np.concatenate(point_blocks, axis=0)
    if color_blocks and sum(len(block) for block in color_blocks) == len(vertices):
        colors = np.concatenate(color_blocks, axis=0)
    else:
        colors = np.full((len(vertices), 3), 190, dtype=np.uint8)

    cloud = trimesh.points.PointCloud(vertices=vertices, colors=colors)
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    cloud.export(output_path)
    return output_path


def reconstruct(files, confidence_percentile, image_size, alignment_iterations, model, device, output_dir, max_images):
    paths = normalize_files(files)
    if len(paths) < 2:
        raise gr.Error("Upload at least two overlapping images of the same indoor scene.")
    if len(paths) > max_images:
        raise gr.Error(f"Please upload no more than {max_images} images.")

    imgs = load_images(paths, size=int(image_size), verbose=False)
    pairs = make_pairs(imgs, scene_graph="complete", prefilter=None, symmetrize=True)
    outputs = inference(pairs, model, device=device, batch_size=1)

    if len(paths) == 2:
        mode = GlobalAlignerMode.PairViewer
    else:
        mode = GlobalAlignerMode.PointCloudOptimizer
    scene = global_aligner(outputs, device=device, mode=mode)
    if mode == GlobalAlignerMode.PointCloudOptimizer:
        scene.compute_global_alignment(
            init="mst", niter=int(alignment_iterations), schedule="linear", lr=0.01
        )

    output_path = os.path.join(output_dir, "dust3r_reconstruction.glb")
    return export_scene(scene, output_path, float(confidence_percentile)), output_path


def main() -> None:
    args = parse_args()
    device = args.device or ("cuda" if torch.cuda.is_available() else "cpu")
    output_dir = args.output_dir or tempfile.mkdtemp(prefix="dust3r_nammaspace_")
    if args.weights:
        model = AsymmetricCroCo3DStereo.from_pretrained(args.weights)
    else:
        model = AsymmetricCroCo3DStereo.from_pretrained(args.model_name)
    model.to(device).eval()

    with gr.Blocks(title="NammaSpace — DUSt3R reconstruction") as app:
        gr.Markdown(
            "# NammaSpace — DUSt3R reconstruction\n"
            "Upload overlapping indoor images. DUSt3R will estimate geometry and camera relationships, "
            "then export a research-quality colored GLB point cloud."
        )
        with gr.Row():
            with gr.Column():
                image_input = gr.File(label="Scene images", file_count="multiple", file_types=["image"], type="filepath")
                confidence = gr.Slider(0, 99, value=50, step=1, label="Discard lowest-confidence percentile")
                resolution = gr.Dropdown([224, 512], value=args.image_size, label="Inference resolution")
                iterations = gr.Slider(50, 500, value=args.alignment_iterations, step=50, label="Global alignment iterations")
                run = gr.Button("Reconstruct with DUSt3R", variant="primary")
            with gr.Column():
                output = gr.Model3D(label="DUSt3R reconstruction (GLB)")
                download = gr.File(label="Download GLB")

        run.click(
            fn=lambda files, conf, size, niter: reconstruct(
                files, conf, size, niter, model, device, output_dir, args.max_images
            ),
            inputs=[image_input, confidence, resolution, iterations],
            outputs=[output, download],
        )

    app.launch(
        server_name=args.server_name or ("0.0.0.0" if args.local_network else None),
        server_port=args.server_port,
    )


if __name__ == "__main__":
    main()
