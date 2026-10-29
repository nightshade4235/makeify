# krpano GLB viewer example

This example embeds the example reconstruction at [`../example outputs/2.glb`](../example%20outputs/2.glb) in a centered, responsive browser viewer. It uses krpano's official ThreeJS plugin, which supports GLB/GLTF files as `type="threejs"` hotspots.

## Setup

The separately licensed krpano runtime files are included in `viewer/krpano/` for this example:

```text
viewer/
  krpano/
    krpano.js
    threejs_krpanoplugin.js
```

Read [`krpano/THIRD_PARTY_LICENSE.md`](krpano/THIRD_PARTY_LICENSE.md) before redistributing or deploying the example. The runtime is not covered by the makeify license.

The XML scene intentionally places the model at the origin with `depth="0"` and `tx="0" ty="0" tz="0"`. The page layout centers the viewer card in the browser viewport. The `scale="100"` setting converts the small source reconstruction into a useful inspection size for krpano's centimeter-based 3D hotspot coordinates.

## Run locally

Serve the repository over HTTP so the browser can load the GLB and krpano assets:

```bash
python3 -m http.server 8000
```

Then open [http://localhost:8000/viewer/](http://localhost:8000/viewer/) in a WebGL-capable browser.

Do not open `index.html` directly with `file://`; browser module and binary-file restrictions can prevent the GLB from loading.
