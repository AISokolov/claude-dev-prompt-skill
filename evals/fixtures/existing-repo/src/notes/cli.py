import argparse
from pathlib import Path

from notes import store

DATA = Path.home() / ".notes.json"


def main() -> None:
    parser = argparse.ArgumentParser(prog="notes")
    sub = parser.add_subparsers(dest="cmd", required=True)
    add = sub.add_parser("add")
    add.add_argument("text")
    ls = sub.add_parser("list")
    ls.add_argument("--page", type=int, default=1)
    args = parser.parse_args()

    notes = store.load(DATA)
    if args.cmd == "add":
        notes.append({"text": args.text})
        store.save(DATA, notes)
    else:
        for n in store.list_page(notes, args.page):
            print(n["text"])


if __name__ == "__main__":
    main()
