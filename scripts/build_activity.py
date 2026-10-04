"""Render the open-source activity card (dark and light) from the GitHub API.

Counts only pull requests by AUTHOR in the allowlisted public repositories, so
the card shows verifiable upstream work. Standard library only. On any API
failure the script exits non-zero and leaves the previous card untouched.

Run: GITHUB_TOKEN=... python3 scripts/build_activity.py
"""
import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from html import escape
from pathlib import Path

AUTHOR = "TheRWX"
REPOS = ["BasedHardware/omi", "BerriAI/litellm"]
ASSETS = Path(__file__).resolve().parent.parent / "assets"

THEMES = {
    "dark": dict(bg="#0b0e15", panel="#111621", border="#22303f", text="#e8edf2", muted="#8aa4b3",
                 grid="#2b9fc4", merged="#2ea043", open="#d4a017", accent="#b3122e"),
    "light": dict(bg="#f5f2eb", panel="#fffdf8", border="#d8d0c0", text="#1b1f24", muted="#56656f",
                  grid="#4f8ea6", merged="#1a7f37", open="#9a6700", accent="#b3122e"),
}


def search(query: str) -> dict:
    url = "https://api.github.com/search/issues?" + urllib.parse.urlencode({"q": query, "per_page": 100})
    headers = {"Accept": "application/vnd.github+json", "User-Agent": f"{AUTHOR}-profile-card"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=30) as resp:
        data = json.load(resp)
    if data.get("incomplete_results"):
        raise RuntimeError(f"incomplete search results for {query!r}")
    return data


def kind(title: str) -> str:
    head = title.split(":", 1)[0].split("(", 1)[0].strip().lower()
    return {"docs": "docs", "fix": "fixes", "feat": "features"}.get(head, "other")


def collect() -> dict:
    repos, kinds = [], {"docs": 0, "fixes": 0, "features": 0, "other": 0}
    for repo in REPOS:
        merged = search(f"type:pr author:{AUTHOR} repo:{repo} is:merged")
        opened = search(f"type:pr author:{AUTHOR} repo:{repo} is:open")
        for item in merged["items"]:
            kinds[kind(item["title"])] += 1
        repos.append({"repo": repo, "merged": merged["total_count"], "open": opened["total_count"]})
    return {
        "author": AUTHOR,
        "repos": repos,
        "merged_by_kind": kinds,
        "updated": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
    }


def render(data: dict, c: dict) -> str:
    merged = sum(r["merged"] for r in data["repos"])
    opened = sum(r["open"] for r in data["repos"])
    active = sum(1 for r in data["repos"] if r["merged"] or r["open"])
    k = data["merged_by_kind"]
    breakdown = " · ".join(f"{n} {label}" for label, n in
                           (("docs", k["docs"]), ("fixes", k["fixes"]), ("features", k["features"]), ("other", k["other"])) if n)
    scale = max([r["merged"] + r["open"] for r in data["repos"]] + [1])
    bars, y = [], 70
    for i, r in enumerate(data["repos"]):
        w_m = round(440 * r["merged"] / scale)
        w_o = round(440 * r["open"] / scale)
        bars.append(f"""
    <text class="label" x="610" y="{y}" fill="{c['text']}">{escape(r['repo'])}</text>
    <text class="label" x="1150" y="{y}" text-anchor="end" fill="{c['muted']}">{r['merged']} merged · {r['open']} open</text>
    <g class="grow" style="animation-delay:{0.3 + i * 0.25:.2f}s">
      <rect x="610" y="{y + 10}" width="540" height="12" rx="6" fill="{c['border']}"/>
      <rect x="610" y="{y + 10}" width="{w_m}" height="12" rx="6" fill="{c['merged']}"/>
      <rect x="{610 + w_m}" y="{y + 10}" width="{w_o}" height="12" rx="6" fill="{c['open']}" opacity="0.85"/>
    </g>""")
        y += 62
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="230" viewBox="0 0 1200 230" role="img" aria-labelledby="t d">
  <title id="t">Open-source activity</title>
  <desc id="d">{merged} merged and {opened} open pull requests by @{AUTHOR} across {active} upstream projects ({escape(breakdown)}). Last change {data['updated']}.</desc>
  <style>
    .num {{ font: 800 46px "Segoe UI", "Helvetica Neue", Arial, sans-serif; }}
    .cap {{ font: 600 13px ui-monospace, "SFMono-Regular", "DejaVu Sans Mono", Menlo, Consolas, monospace; letter-spacing: 2px; }}
    .label {{ font: 600 15px ui-monospace, "SFMono-Regular", "DejaVu Sans Mono", Menlo, Consolas, monospace; }}
    .head {{ font: 700 14px ui-monospace, "SFMono-Regular", "DejaVu Sans Mono", Menlo, Consolas, monospace; letter-spacing: 3px; }}
    .grow {{ transform-box: fill-box; transform-origin: left; animation: grow 1.1s cubic-bezier(.2,.8,.2,1) both; }}
    .rise {{ animation: rise .8s ease-out both; }}
    .led {{ animation: led 2.4s ease-in-out infinite; }}
    @keyframes grow {{ from {{ transform: scaleX(0); }} to {{ transform: scaleX(1); }} }}
    @keyframes rise {{ from {{ opacity: 0; transform: translateY(8px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes led {{ 50% {{ opacity: .25; }} }}
    @media (prefers-reduced-motion: reduce) {{ .grow, .rise, .led {{ animation: none; }} }}
  </style>
  <rect x="1" y="1" width="1198" height="228" rx="14" fill="{c['panel']}" stroke="{c['border']}" stroke-width="2"/>
  <rect x="1" y="1" width="1198" height="6" rx="3" fill="{c['accent']}"/>
  <circle class="led" cx="44" cy="44" r="6" fill="{c['merged']}"/>
  <text class="head" x="60" y="49" fill="{c['muted']}">UPSTREAM ACTIVITY</text>

  <g class="rise" style="animation-delay:.1s">
    <text class="num" x="40" y="128" fill="{c['merged']}">{merged}</text>
    <text class="cap" x="40" y="152" fill="{c['muted']}">MERGED PRs</text>
  </g>
  <g class="rise" style="animation-delay:.25s">
    <text class="num" x="220" y="128" fill="{c['open']}">{opened}</text>
    <text class="cap" x="220" y="152" fill="{c['muted']}">OPEN PRs</text>
  </g>
  <g class="rise" style="animation-delay:.4s">
    <text class="num" x="390" y="128" fill="{c['text']}">{active}</text>
    <text class="cap" x="390" y="152" fill="{c['muted']}">PROJECTS</text>
  </g>
  <text class="cap" x="40" y="196" fill="{c['muted']}">MERGED: {escape(breakdown.upper())}</text>
  <line x1="580" y1="40" x2="580" y2="200" stroke="{c['border']}" stroke-width="2"/>
  {''.join(bars)}
  <text class="cap" x="1150" y="212" text-anchor="end" fill="{c['muted']}">GITHUB API · LAST CHANGE {data['updated']}</text>
</svg>
"""


def main() -> int:
    try:
        data = collect()
    except Exception as e:  # keep the last good card rather than publishing zeros
        print(f"GitHub API query failed, keeping the previous card: {e}", file=sys.stderr)
        return 1
    ASSETS.mkdir(exist_ok=True)
    previous = ASSETS / "activity.json"
    if previous.exists():
        old = json.loads(previous.read_text(encoding="utf-8"))
        if {k: v for k, v in old.items() if k != "updated"} == {k: v for k, v in data.items() if k != "updated"}:
            data["updated"] = old["updated"]  # numbers unchanged: keep files identical, no commit
    for name, colors in THEMES.items():
        (ASSETS / f"activity-{name}.svg").write_text(render(data, colors), encoding="utf-8")
    (ASSETS / "activity.json").write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(data))
    return 0


if __name__ == "__main__":
    sys.exit(main())
