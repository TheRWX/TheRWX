"""Render the animated profile header (dark and light) to assets/.

Self-contained SVG: CSS animations only, system fonts, no external resources.
All motion stops under prefers-reduced-motion, leaving a complete static image.

Run: python3 scripts/build_header.py
"""
from pathlib import Path

ASSETS = Path(__file__).resolve().parent.parent / "assets"

THEMES = {
    "dark": dict(bg="#07090f", grid="#2b9fc4", grid_op="0.45", text="#e8edf2", muted="#8aa4b3",
                 face_top="#2a2d33", face_bottom="#b3122e", outline="#ffffff", shine="#ffffff", vignette="#000000"),
    "light": dict(bg="#f5f2eb", grid="#4f8ea6", grid_op="0.22", text="#1b1f24", muted="#4d5e69",
                  face_top="#30343b", face_bottom="#b3122e", outline="#1b1f24", shine="#ffffff", vignette="#d9d2c3"),
}

SUBTITLE = "OPEN-SOURCE CONTRIBUTOR  ·  PYTHON  ·  MOBILE  ·  EMBEDDED"

TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="300" viewBox="0 0 1200 300" role="img" aria-labelledby="t d">
  <title id="t">RWX</title>
  <desc id="d">RWX (@TheRWX): open-source contributor working in Python, mobile and embedded software.</desc>
  <defs>
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M40 0H0V40" fill="none" stroke="{grid}" stroke-width="1"/>
    </pattern>
    <linearGradient id="face" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{face_top}"/>
      <stop offset="0.48" stop-color="{face_top}"/>
      <stop offset="0.52" stop-color="{face_bottom}"/>
      <stop offset="1" stop-color="#5e0a18"/>
    </linearGradient>
    <linearGradient id="shine" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="{shine}" stop-opacity="0"/>
      <stop offset="0.5" stop-color="{shine}" stop-opacity="0.75"/>
      <stop offset="1" stop-color="{shine}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="scan" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{grid}" stop-opacity="0"/>
      <stop offset="1" stop-color="{grid}" stop-opacity="0.35"/>
    </linearGradient>
    <radialGradient id="vignette" cx="0.5" cy="0.5" r="0.75">
      <stop offset="0.55" stop-color="{vignette}" stop-opacity="0"/>
      <stop offset="1" stop-color="{vignette}" stop-opacity="0.85"/>
    </radialGradient>
    <clipPath id="word"><text x="600" y="200" text-anchor="middle" class="mark">RWX</text></clipPath>
    <clipPath id="frame"><rect width="1200" height="300" rx="14"/></clipPath>
  </defs>
  <style>
    .mark {{ font: 900 150px "Arial Black", "Helvetica Neue", Arial, sans-serif; letter-spacing: 6px; }}
    .mono {{ font: 600 17px ui-monospace, "SFMono-Regular", "DejaVu Sans Mono", Menlo, Consolas, monospace; letter-spacing: 3px; }}
    .small {{ font: 500 13px ui-monospace, "SFMono-Regular", "DejaVu Sans Mono", Menlo, Consolas, monospace; letter-spacing: 2px; }}
    .drift {{ animation: drift 8s linear infinite; }}
    .scan {{ animation: scan 6s linear infinite; }}
    .sweep {{ animation: sweep 7s ease-in-out infinite; }}
    .type {{ animation: type 2.6s steps(52, end) 0.6s both; }}
    .cursor {{ animation: blink 1s step-end infinite; }}
    @keyframes drift {{ from {{ transform: translateY(0); }} to {{ transform: translateY(40px); }} }}
    @keyframes scan {{ from {{ transform: translateY(-80px); }} to {{ transform: translateY(320px); }} }}
    @keyframes sweep {{ 0%, 55% {{ transform: translateX(-420px); }} 85%, 100% {{ transform: translateX(1240px); }} }}
    @keyframes type {{ from {{ clip-path: inset(0 100% 0 0); }} to {{ clip-path: inset(0 0 0 0); }} }}
    @keyframes blink {{ 50% {{ opacity: 0; }} }}
    @media (prefers-reduced-motion: reduce) {{
      .drift, .scan, .sweep, .cursor {{ animation: none; }}
      .scan, .sweep {{ display: none; }}
      .type {{ animation: none; }}
    }}
  </style>
  <g clip-path="url(#frame)">
    <rect width="1200" height="300" fill="{bg}"/>
    <g class="drift" opacity="{grid_op}"><rect y="-40" width="1200" height="380" fill="url(#grid)"/></g>
    <rect class="scan" x="0" y="0" width="1200" height="80" fill="url(#scan)"/>
    <rect width="1200" height="300" fill="url(#vignette)"/>

    <rect y="34" width="1200" height="3" fill="#d4a017"/>
    <rect y="40" width="1200" height="22" fill="#9e1028"/>
    <rect y="65" width="1200" height="3" fill="#d4a017"/>

    <text x="600" y="200" text-anchor="middle" class="mark" fill="url(#face)" stroke="{outline}" stroke-width="7" stroke-linejoin="round" paint-order="stroke"/>
    <text x="600" y="200" text-anchor="middle" class="mark" fill="url(#face)" stroke="#9e1028" stroke-width="2.5" stroke-linejoin="round">RWX</text>
    <g clip-path="url(#word)"><rect class="sweep" x="0" y="80" width="220" height="140" fill="url(#shine)" transform="translate(-420 0)"/></g>

    <g transform="translate(600 252)">
      <text class="mono type" text-anchor="middle" fill="{text}">{subtitle}</text>
    </g>
    <text class="small" x="34" y="284" fill="{muted}">@TheRWX</text>
    <text class="small" x="1166" y="284" text-anchor="end" fill="{muted}">US · MOUNTAIN TIME <tspan class="cursor" fill="#d4a017">█</tspan></text>
  </g>
</svg>
"""


def main():
    ASSETS.mkdir(exist_ok=True)
    for name, colors in THEMES.items():
        svg = TEMPLATE.format(subtitle=SUBTITLE, **colors)
        # The outline layer needs the glyphs too (kept separate so the stroke sits behind the face)
        svg = svg.replace('paint-order="stroke"/>', 'paint-order="stroke">RWX</text>', 1)
        (ASSETS / f"header-{name}.svg").write_text(svg, encoding="utf-8")
        print(f"wrote assets/header-{name}.svg")


if __name__ == "__main__":
    main()
