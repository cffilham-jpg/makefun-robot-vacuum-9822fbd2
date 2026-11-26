"""Write the robot vacuum's one-line excuse to the configured output file.
The Lego joke was chosen for a specific obstacle and an immediate peace-making surrender.
"""

import os
from pathlib import Path


LINE = "I saw the Lego and chose peace."

if not LINE.strip():
    raise ValueError("The entry line must not be empty or whitespace-only.")
if len(LINE) > 120:
    raise ValueError("The entry line must be at most 120 characters.")

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))
