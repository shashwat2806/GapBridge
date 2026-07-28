import json
from pathlib import Path


def load_framework(json_path: str) -> list:
    path = Path(json_path)

    if not path.exists():
        raise FileNotFoundError(f"Framework file not found: {path}")

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data["controls"]