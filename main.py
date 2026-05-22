"""
main.py
-------
Entry point for the Modular Modern House Builder tool.
Sets up sys.path so Maya can locate the project modules, then runs
the full house build by calling build_all() from core_utils.

Run this file directly in the Maya Script Editor to build the house.

Author: [Your Name]
Course: [Course Name]
"""

import sys
import os

# ---------------------------------------------------------------------------
# sys.path block — ensures Maya can find all project modules.
# Update this path to wherever you saved the project files.
# ---------------------------------------------------------------------------
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

# ---------------------------------------------------------------------------
# Project imports
# ---------------------------------------------------------------------------
import maya.cmds as cmds
from core_utils import build_all, CONFIG

# ---------------------------------------------------------------------------
# SELF-TEST — runs when this file is executed directly in Maya
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=" * 60)
    print("  Modular Modern House Builder — Self Test")
    print("=" * 60)
    print(f"  Config entries loaded : {len(CONFIG)}")
    print(f"  Starting build...")
    print("=" * 60)

    created_objects = build_all()

    print("=" * 60)
    print(f"  Build finished. {len(created_objects)} objects in viewport.")
    print("=" * 60)

    # Frame all objects in the viewport so the house is visible
    cmds.viewFit(all=True)
