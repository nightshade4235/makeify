# krpano GLB viewer example

This example embeds the example reconstruction at [`../example outputs/2.glb`](../example%20outputs/2.glb) in a centered, responsive browser viewer. It uses krpano's official ThreeJS plugin, which supports GLB/GLTF files as `type="threejs"` hotspots.

## Setup

krpano distributes `krpano.js` and `threejs_krpanoplugin.js` with its licensed viewer package. Copy those files into this directory without committing licensed binaries:

```text
viewer/
  krpano/
    krpano.js
    threejs_krpanoplugin.js
```

The XML scene intentionally places the model at the origin with `depth="0"` and `tx="0" ty="0" tz="0"`. The page layout centers the viewer card in the browser viewport. The `scale="100"` setting converts the small source reconstruction into a useful inspection size for krpano's centimeter-based 3D hotspot coordinates.

## Run locally

Serve the repository over HTTP so the browser can load the GLB and krpano assets:

```bash
python3 -m http.server 8000
```

Then open [http://localhost:8000/viewer/](http://localhost:8000/viewer/) in a WebGL-capable browser.

Do not open `index.html` directly with `file://`; browser module and binary-file restrictions can prevent the GLB from loading.
