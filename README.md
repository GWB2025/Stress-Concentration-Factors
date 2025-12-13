# Stress Concentration Factors (U-Groove)

Interactive, single‑page calculator for stress concentration factors (Kt) of a grooved shaft under axial, bending, and torsion loading. Enter the shaft geometry and the page evaluates Kt using tabulated coefficient polynomials with automatic range checks.

## Try it in the browser

- GitHub Pages (after enabling in repo settings): `https://gwb2025.github.io/Stress-Concentration-Factors/`
  - In GitHub: Settings → Pages → Deploy from branch → `master` (or `main` if you rename) → `/ (root)`. Save, then open the link above once it builds.

## How it works

- Inputs: outside diameter `D`, groove depth `h`, fillet radius `r`.
- Validates positive inputs and that reduced diameter `d = D - 2h` stays positive.
- Uses `h/r` to pick coefficient sets (axial ≥ 0.1; bending/torsion ≥ 0.25; capped at 50) and switches forms at `h/r = 2`.
- Computes Kt via cubic polynomials in `x = 2h / D` for each loading case.
- Displays formatted results; shows errors for out-of-range or invalid inputs.

## Local development

```bash
# from repo root
python server.py
# open http://127.0.0.1:8000
```

The app is static (`index.html`, images) and requires no build step.

## Files

- `index.html` — UI, styling, and Kt calculations.
- `server.py` — tiny HTTP server for local preview.
- `bending.png`, `tension.png`, `Torsion.png` — reference visuals.
- `.gitignore` — standard Python/editor/OS ignores.
