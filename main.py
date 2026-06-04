"""
main.py
-------
Entry point for the Modular Modern House Builder tool.
Sets up sys.path so Maya can locate the project modules, builds the full
house geometry via build_all(), then applies all three materials via
build_all_materials().

Run this file directly in the Maya Script Editor to build the house.

Author: Jillian Richards
Course: DIGM 131
"""

import sys
import os

# sys.path block — ensures Maya can find all project modules.
# Update this path to wherever you saved the project files.
PROJECT_DIR = os.path.dirname(os.path.abspath("C:\Users\jilli\OneDrive - Drexel University\Third Year\DIGM131\Final\Modern_Building\scripts\DIGM-131-003-Final-main\house_builder"))
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)

# Project imports
import maya.cmds as cmds
from core_utils import build_all, CONFIG
from materials import build_all_materials

# SELF-TEST — runs when this file is executed directly in Maya
if __name__ == "__main__":
    print("=" * 60)
    print("  Modular Modern House Builder — Self Test")
    print("=" * 60)
    print(f"  Config entries loaded : {len(CONFIG)}")
    print(f"  Step 1: Building geometry...")
    print("=" * 60)

    # Step 1 — build all geometry
    created_objects = build_all()

    print("=" * 60)
    print(f"  Geometry complete: {len(created_objects)} objects created.")
    print(f"  Step 2: Applying materials...")
    print("=" * 60)

    # Step 2 — create and assign all materials
    build_all_materials()

    print("=" * 60)
    print("  Build and materials complete.")
    print("=" * 60)

    # Frame all objects in the viewport
    cmds.viewFit(all=True)
