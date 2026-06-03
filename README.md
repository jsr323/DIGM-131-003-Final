Maya Modular Modern House Builder
Author: Jillian Richards DIGM131

A Maya Python tool that builds a modern house scene from a data-driven config list.
Includes a custom UI window, Arnold materials, and full error handling.

File Structure
main.py #Entry point - runs geometry, materials, and open UI
builder.py #Core geometry functions (one per element type)
core_utils.py #CONFIG list, BUILDERS dict, dispatcher, driver loop
materials.py #Arnold material creation and assignment
ui.py #Custom Maya UI window
README.md

How to Run
Save all files to one folder
Open Maya -> Script Editor -> Python tab
Paste and run:

import sys
sys.path.insert(0, "C:/YOUR/PATH/TO/PROJECT")  # update this

import importlib
import builder, core_utils, materials, ui
importlib.reload(builder)
importlib.reload(core_utils)
importlib.reload(materials)
importlib.reload(ui)

exec(open("C:/YOUR/PATH/TO/PROJECT/main.py").read())

Key Functions
create_wall()             builder.py   Wall segment polyCube
create_floor()            builder.py   Floor slab polyCube
create_roof()             builder.py   Roof panel polyCube
create_fence()            builder.py   Fence segment polyCube
create_pillar()           builder.py   Pillar polyCube
create_flower_bed()       builder.py   Landscape volume polyCube
create_stair()            builder.py   Stair step polyCube
create_element()          core_utils.py   Dispatcher using ** unpacking
build_all()               core_utils.py   Driver loop through full CONFIG
build_all_materials()     materials.py   Creates and assigns all 3 materials
open_house_builder_ui()   ui.py   Opens the Maya UI window

Requirments
Autodesk Maya 2024+
Arnold renderer
Python 3 (Maya built-in)
