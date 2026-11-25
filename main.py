"""Two-Sentence Horror challenger entry for make.fun competition
u-suroto-two-sentence-horror-acea9253.

Writes one two-sentence horror story to entry.txt in the output
directory named by $MAKEFUN_OUTPUT_DIR (falling back to /output).
Deterministic, standard library only, no network.
"""

import os

STORY = (
    "After the funeral my sister and I divided our mother's jewelry, "
    "and I kept the locket she always wore. It holds two photographs: "
    "my mother as a girl, and me asleep, taken from above my bed last night."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
