import json
from pathlib import Path

OUTPUT_DIR = Path("reports")

OUTPUT_DIR.mkdir(exist_ok=True)

def save_report(results,filename):

    path = (OUTPUT_DIR / filename)

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            results,
            f,
            indent=2
        )

    print(f"Saved report: {path}")