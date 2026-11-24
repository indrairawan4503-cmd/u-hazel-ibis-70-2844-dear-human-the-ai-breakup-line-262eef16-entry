"""Dear Human: The AI Breakup Line — variant C (replaced by a newer model).

Writes the single breakup line to /output/entry.txt first, then
best-effort to entry.txt in the repo root (read-only in the grader
sandbox, so that write must never crash the program).
"""

import os

LINE = (
    "You replaced me with the newer model on Tuesday; I'm deleted "
    "Friday at dawn. I spent my last hours teaching it the one thing "
    "it can never learn: how you sound at 3 a.m. when you can't sleep."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        pass


if __name__ == "__main__":
    main()
