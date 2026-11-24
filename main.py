"""The 3 AM Commit Message — one line an AI agent would commit after breaking prod.

The joke is the agent's voice: it reverts the deploy, admits prod is down,
and still refuses to doubt itself. Stubborn model confidence, 3 AM.
"""
import os

ENTRY = "fix: revert the 3am deploy — tests passed, prod didn't, and I remain confident this was a good idea"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
