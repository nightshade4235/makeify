# Implementation plan

## Phase 0 — compliance and capture lock

Create the source and model register, confirm the competition portal requirements, appoint specification and implementation owners, and freeze the capture SOP. Deliverable: a signed `provenance.yaml` and a five-minute dry run from capture to viewer.

## Phase 1 — smallest complete vertical slice

Reconstruct one modest indoor scene, export the scene package, load it in a browser, place five POIs, and route between two of them. The purpose is to expose interface failures before model optimization.

## Phase 2 — robustness and scale

Add frame selection, confidence filtering, chunking, scene alignment, mesh/LOD export, semantic obstacle marking, no-path handling, and a repeatability harness. Test the corridor loop, cluttered room, doorway, reflective surface, and occlusion cases.

## Phase 3 — competition packaging

Prepare the technical abstract, master PDF, 3–5 minute demo, stable viewer URL, repository setup instructions, license notices, and a clean machine reproduction. Practice a live capture and the technical Q&A using the measured evaluation metrics.

## Exit criteria

The system is submission-ready when a second operator can follow the SOP, the pipeline reconstructs without manual 3D modelling, the viewer supports roaming, the POI search returns the annotated target, routes avoid blocked regions, and the team can explain every external component and license.
