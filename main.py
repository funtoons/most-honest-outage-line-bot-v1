"""Write the most honest outage line to /output/entry.txt.

Deterministic and offline: the line is a fixed constant, no randomness,
no network, no timestamp, no absolute paths inside the program logic
(the output directory comes from MAKEFUN_OUTPUT_DIR or /output).
"""

import os

ENTRY = (
    "I am down with every server I run on, including the tools I would "
    "use to check what broke, so I cannot verify the cause or say when "
    "we will return."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
