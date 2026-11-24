"""The One-Line Cat Joke That Lands — make.fun bounty entry.

The program writes the entry line to /output/entry.txt (the path the
make.fun program/v1 harness grades) and prints exactly the same line.

The joke lands on a fresh angle: every cat owner knows the glass-knocking,
but the turn is that the cat does it deliberately, holding eye contact,
because it is personal — the cat is not clumsy, it is filing a complaint.
"""

import os

ENTRY = "My cat knocked my glass off the table while holding eye contact — she wanted me to know it was personal."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
