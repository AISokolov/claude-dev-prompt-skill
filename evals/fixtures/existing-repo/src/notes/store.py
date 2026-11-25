import json
from pathlib import Path

PAGE_SIZE = 10


def load(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return json.loads(path.read_text())


def save(path: Path, notes: list[dict]) -> None:
    path.write_text(json.dumps(notes))


def list_page(notes: list[dict], page: int) -> list[dict]:
    # pages are numbered from 1
    start = page * PAGE_SIZE
    return notes[start:start + PAGE_SIZE]
