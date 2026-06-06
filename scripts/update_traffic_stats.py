"""Update README traffic totals from GitHub traffic APIs.

GitHub exposes traffic history for a recent window only. This script stores
daily traffic rows in .github/traffic-history.json and computes cumulative
display totals from the saved history.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
HISTORY = ROOT / ".github" / "traffic-history.json"
TRAFFIC_START = "<!-- traffic:start -->"
TRAFFIC_END = "<!-- traffic:end -->"
DEFAULT_REPOSITORY = "XinzeLee/Fundamentals_of_AI_for_PE"


def api_get(path: str) -> dict:
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("GH_TOKEN or GITHUB_TOKEN is required to read GitHub traffic data.")

    repository = os.environ.get("GITHUB_REPOSITORY", DEFAULT_REPOSITORY)
    url = f"https://api.github.com/repos/{repository}{path}"
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "traffic-stats-updater",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"GitHub API request failed: {exc.code} {detail}") from exc


def load_history() -> dict:
    if not HISTORY.exists():
        return {"views": {}, "clones": {}}
    return json.loads(HISTORY.read_text(encoding="utf-8"))


def merge_daily_rows(history: dict, key: str, rows: list[dict]) -> None:
    bucket = history.setdefault(key, {})
    for row in rows:
        date = str(row["timestamp"])[:10]
        bucket[date] = {
            "count": int(row.get("count", 0)),
            "uniques": int(row.get("uniques", 0)),
        }


def totals(history: dict, key: str) -> tuple[int, int]:
    rows = history.get(key, {}).values()
    return (
        sum(int(row.get("count", 0)) for row in rows),
        sum(int(row.get("uniques", 0)) for row in rows),
    )


def fmt(n: int) -> str:
    return f"{n:,}"


def render_block(history: dict) -> str:
    views, unique_visitors = totals(history, "views")
    clones, unique_clones = totals(history, "clones")
    updated = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    return f"""{TRAFFIC_START}
<p align="center">
  <a href="https://github.com/XinzeLee/Fundamentals_of_AI_for_PE/graphs/traffic">
    <img src="https://img.shields.io/badge/Views-GitHub_Insights-2563eb?style=flat-square" alt="Repository views on GitHub Insights" />
  </a>
  <a href="https://github.com/XinzeLee/Fundamentals_of_AI_for_PE/graphs/traffic">
    <img src="https://img.shields.io/badge/Unique_visitors-GitHub_Insights-0f766e?style=flat-square" alt="Unique repository visitors on GitHub Insights" />
  </a>
  <a href="https://github.com/XinzeLee/Fundamentals_of_AI_for_PE/graphs/traffic">
    <img src="https://img.shields.io/badge/Clones-GitHub_Insights-7c3aed?style=flat-square" alt="Repository clones on GitHub Insights" />
  </a>
  <a href="https://github.com/XinzeLee/Fundamentals_of_AI_for_PE/graphs/traffic">
    <img src="https://img.shields.io/badge/Unique_clones-GitHub_Insights-b45309?style=flat-square" alt="Unique repository clones on GitHub Insights" />
  </a>
</p>

| Traffic indicator | Cumulative value |
|---|---:|
| Views | {fmt(views)} |
| Unique visitors | {fmt(unique_visitors)} |
| Clones | {fmt(clones)} |
| Unique clones | {fmt(unique_clones)} |

<sub>Updated weekly from GitHub traffic data. Cumulative values start from the first successful updater run. GitHub reports unique visitors/clones per day, so unique totals are accumulated daily unique counts. Last updated: {updated} UTC.</sub>
{TRAFFIC_END}"""


def update_readme(history: dict) -> None:
    readme = README.read_text(encoding="utf-8")
    block = render_block(history)
    pattern = re.compile(
        rf"{re.escape(TRAFFIC_START)}.*?{re.escape(TRAFFIC_END)}",
        flags=re.DOTALL,
    )
    if pattern.search(readme):
        readme = pattern.sub(block, readme, count=1)
    else:
        readme = readme.replace(
            "# Fundamentals of AI for PE — repository overview\n",
            f"# Fundamentals of AI for PE — repository overview\n\n{block}\n",
            1,
        )
    README.write_text(readme, encoding="utf-8", newline="\n")


def main() -> int:
    history = load_history()
    views = api_get("/traffic/views")
    clones = api_get("/traffic/clones")
    merge_daily_rows(history, "views", views.get("views", []))
    merge_daily_rows(history, "clones", clones.get("clones", []))

    HISTORY.parent.mkdir(parents=True, exist_ok=True)
    HISTORY.write_text(json.dumps(history, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    update_readme(history)
    return 0


if __name__ == "__main__":
    sys.exit(main())
