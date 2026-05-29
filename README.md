Maya Modular Modern House Builder
I wrote this in the CODE mode not the Preview Mode, so it looks crazy if it is not in the Code tab... Sorry!

A Maya Python automation tool that procedurally builds a modern house scene
from a data-driven configuration list. Each architectural element — walls,
floors, roofs, fences, pillars, flower beds, and stairs — is defined as a
dictionary entry and routed through a dispatcher to the correct builder
function, which places a polyCube primitive in the Maya viewport.
Built as a final project for DIGM 131 — Jillian Richards — 003

File Structure
maya-house-builder/
│
├── main.py              # Entry point, sys.path setup, self-test runner
├── core_utils.py        # CONFIG list, BUILDERS dict, create_element(), build_all()
├── builder.py           # All geometry builder functions (one per element type)
│
└── README.md

How to Run

Copy all .py files into the same folder on your computer.
Open Autodesk Maya.
Open the Script Editor (Windows → General Editors → Script Editor).
Set the tab to Python.
Paste and run the following:

pythonimport sys
sys.path.insert(0, "C:/YOUR/PATH/TO/PROJECT")  # update this path
import main
The full house will build in the viewport automatically.

Function List
  builder.py
  FunctionDescriptioncreate_wall(name, width, height, depth, tx, ty, tz, rx, ry, rz)Creates a wall segment as a polyCube
  create_floor(name, width, height, depth, tx, ty, tz, rx, ry, rz)Creates a floor slab as a polyCube
  create_roof(name, width, height, depth, tx, ty, tz, rx, ry, rz)Creates a roof panel as a polyCube
  create_fence(name, width, height, depth, tx, ty, tz, rx, ry, rz)Creates a fence segment as a polyCube
  create_pillar(name, width, height, depth, tx, ty, tz, rx, ry, rz)Creates a structural pillar as a polyCube
  create_flower_bed(name, width, height, depth, tx, ty, tz, rx, ry, rz)Creates a landscape flower bed volume as a polyCube
  create_stair(name, width, height, depth, tx, ty, tz, rx, ry, rz)Creates a single stair step as a polyCube

All builder functions share the same parameter pattern:

Default values on every parameter so functions are safe to call with no arguments
Input validation — negative or zero size values are caught with cmds.warning() and skipped
try/except around all Maya commands so one failure never crashes the full build

core_utils.py
create_element(entry)Dispatcher — routes a config dict to the correct builder function
build_all()Driver loop — iterates over the full CONFIG list and builds every element

main.py
BlockDescriptionsys.path blockAdds the project folder to Python's path so Maya can find the modulesif
__name__ == "__main__"Self-test that calls build_all() and fits the scene in the viewport

Config Data
core_utils.py contains a CONFIG list of 60+ entries across 7 element types:
Type - Count - Description
Wall - 17 - Interior and exterior wall panels
Floor - 10 - Floor slabs at multiple levels
Fence - 6 - Perimeter fence segments
Roof - 2 - Flat roof panels
Pillar - 5 - Structural and decorative columns
Flowerbed - 13 - Landscaping volumes
Stair - 9 - Individual stair steps

Each entry follows this structure:
python{
    "type": "wall",
    "name": "Wall1",
    "width": 4.0, "height": 1.0, "depth": 10.0,
    "tx": -2.0,  "ty": 18.0,   "tz": -9.5,
    "rx": -90,   "ry": 0,      "rz": 0
}

Error Handling

Every builder function validates that width, height, and depth are all > 0
Every builder function wraps Maya commands in try/except and issues a cmds.warning() on failure
create_element() catches unknown type names and skips them with a warning
create_element() wraps each builder call in try/except so one bad entry never stops the loop


Debug Mode
Set DEBUG = True at the top of core_utils.py to enable detailed print output
showing each element's name and type as it is built, plus confirmation when the
Maya object is successfully created.



Checklist O Done  X Not Done

O Project runs without errors
O 2+ modules (builder.py + core_utils.py + main.py)
O 3+ builder functions with docstrings and defaults (7 functions)
O Materials.py with 3 materials
O Config data list with 8+ entries (60+ entries)
O BUILDERS dispatcher dict
O create_element() dispatcher
O Driver loop that processes all entries
O Self-test in if name guard
O README with project description, file structure, function list
O Error handling (try/except) in every builder function
O Input validation (negative/zero values caught with warnings)
O DEBUG flag with print statements
O cmds.warning for user messages
O Module docstrings on every .py file
