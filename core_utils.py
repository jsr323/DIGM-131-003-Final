"""
core_utils.py
-------------
Data-driven configuration and dispatcher engine for the Modular Modern
House Builder tool. Contains the full house layout config list, the
BUILDERS dispatcher dictionary, and the create_element() routing function.

Author: Jillian Richards
Course: DIGM 131
"""

import maya.cmds as cmds
from builder import (
    create_wall,
    create_floor,
    create_roof,
    create_fence,
    create_pillar,
    create_flower_bed,
    create_stair,
)

# DEBUG FLAG — set to True to print detailed trace output
DEBUG = True

# BUILDERS — dispatcher dictionary mapping type names to builder functions
BUILDERS = {
    "wall":       create_wall,
    "floor":      create_floor,
    "roof":       create_roof,
    "fence":      create_fence,
    "pillar":     create_pillar,
    "flowerbed":  create_flower_bed,
    "stair":      create_stair,
}

# CONFIG — full house layout data (8+ entries, 7 element types)
# Each entry maps directly to a builder function via the "type" key.
# Maybe there was a better way to do this because this took forever...
CONFIG = [

    # WALLS
    {"type": "wall", "name": "Wall1",  "width": 4.0,  "height": 1.0, "depth": 10.0, "tx": -2.0,  "ty": 18.0, "tz": -9.5,  "rx": -90, "ry": 0,   "rz": 0},
    {"type": "wall", "name": "Wall2",  "width": 10.0, "height": 1.0, "depth": 10.0, "tx": -5.0,  "ty": 18.0, "tz": 9.5,   "rx": -90, "ry": 0,   "rz": 0},
    {"type": "wall", "name": "Wall3",  "width": 18.5, "height": 0.5, "depth": 7.0,  "tx": 0.0,   "ty": 9.0,  "tz": -4.0,  "rx": -90, "ry": 0,   "rz": 0},
    {"type": "wall", "name": "Wall4",  "width": 20.0, "height": 0.5, "depth": 7.0,  "tx": 2.0,   "ty": 9.0,  "tz": 0.0,   "rx": -90, "ry": 90,  "rz": 0},
    {"type": "wall", "name": "Wall5",  "width": 20.0, "height": 1.0, "depth": 7.0,  "tx": -9.0,  "ty": 9.0,  "tz": 0.0,   "rx": -90, "ry": 90,  "rz": 0},
    {"type": "wall", "name": "Wall6",  "width": 11.0, "height": 0.5, "depth": 7.0,  "tx": -3.5,  "ty": 9.0,  "tz": 10.0,  "rx": -90, "ry": 0,   "rz": 0},
    {"type": "wall", "name": "Wall7",  "width": 11.0, "height": 0.5, "depth": 7.0,  "tx": -3.5,  "ty": 9.0,  "tz": -10.0, "rx": -90, "ry": 0,   "rz": 0},
    {"type": "wall", "name": "Wall8",  "width": 10.0, "height": 0.5, "depth": 7.0,  "tx": 0.0,   "ty": 9.0,  "tz": -5.0,  "rx": -90, "ry": 90,  "rz": 0},
    {"type": "wall", "name": "Wall9",  "width": 20.0, "height": 2.0, "depth": 5.0,  "tx": 0.0,   "ty": -3.0, "tz": -9.0,  "rx": -90, "ry": 0,   "rz": 0},
    {"type": "wall", "name": "Wall10", "width": 8.0,  "height": 2.0, "depth": 5.0,  "tx": 10.0,  "ty": 3.0,  "tz": -4.0,  "rx": -90, "ry": 90,  "rz": 0},
    {"type": "wall", "name": "Wall11", "width": 12.0, "height": 2.0, "depth": 5.0,  "tx": -9.0,  "ty": 3.0,  "tz": -4.0,  "rx": -90, "ry": 90,  "rz": 0},
    {"type": "wall", "name": "Wall12", "width": 4.0,  "height": 1.0, "depth": 10.0, "tx": -8.0,  "ty": 18.0, "tz": -9.5,  "rx": -90, "ry": 0,   "rz": 0},
    {"type": "wall", "name": "Wall13", "width": 14.0, "height": 1.0, "depth": 14.0, "tx": -4.5,  "ty": 7.5,  "tz": -17.0, "rx": 90,  "ry": 0,   "rz": 0},
    {"type": "wall", "name": "Wall14", "width": 14.0, "height": 1.0, "depth": 14.0, "tx": -4.5,  "ty": 7.5,  "tz": -30.0, "rx": 90,  "ry": 0,   "rz": 0},
    {"type": "wall", "name": "Wall15", "width": 14.0, "height": 0.0, "depth": 14.0, "tx": -11.0, "ty": 7.5,  "tz": -23.5, "rx": 90,  "ry": 90,  "rz": 0},
    {"type": "wall", "name": "Wall16", "width": 14.5, "height": 0.5, "depth": 13.0, "tx": 4.0,   "ty": 7.0,  "tz": -22.5, "rx": -90, "ry": 0,   "rz": 0},
    {"type": "wall", "name": "Wall17", "width": 6.5,  "height": 0.2, "depth": 9.0,  "tx": 2.0,   "ty": 9.0,  "tz": -26.2, "rx": -90, "ry": 90,  "rz": 0},

    # FLOORS
    {"type": "floor", "name": "Floor1",  "width": 23.0, "height": 1.0, "depth": 21.0, "tx": 0.0,  "ty": 13.0, "tz": 0.0,   "rx": 0, "ry": 0,  "rz": 0},
    {"type": "floor", "name": "Floor2",  "width": 25.0, "height": 1.0, "depth": 21.0, "tx": 0.0,  "ty": 5.0,  "tz": 0.0,   "rx": 0, "ry": 0,  "rz": 0},
    {"type": "floor", "name": "Floor3",  "width": 20.0, "height": 0.1, "depth": 18.0, "tx": 0.0,  "ty": 0.5,  "tz": 0.0,   "rx": 0, "ry": 0,  "rz": 0},
    {"type": "floor", "name": "Floor4",  "width": 8.0,  "height": 1.0, "depth": 7.0,  "tx": -5.0, "ty": 13.0, "tz": -13.5, "rx": 0, "ry": 0,  "rz": 0},
    {"type": "floor", "name": "Floor5",  "width": 22.0, "height": 0.1, "depth": 13.0, "tx": 0.2,  "ty": 0.5,  "tz": -23.0, "rx": 0, "ry": 0,  "rz": 0},
    {"type": "floor", "name": "Floor6",  "width": 4.5,  "height": 0.5, "depth": 12.0, "tx": 18.5, "ty": 3.8,  "tz": -16.5, "rx": 0, "ry": 0,  "rz": 0},
    {"type": "floor", "name": "Floor7",  "width": 7.0,  "height": 0.5, "depth": 7.5,  "tx": 5.5,  "ty": 5.0,  "tz": -13.5, "rx": 0, "ry": 0,  "rz": 0},
    {"type": "floor", "name": "Floor8",  "width": 7.0,  "height": 0.5, "depth": 12.0, "tx": 8.5,  "ty": 4.5,  "tz": -19.0, "rx": 0, "ry": 90, "rz": 0},
    {"type": "floor", "name": "Floor9",  "width": 7.0,  "height": 0.5, "depth": 2.0,  "tx": 15.5, "ty": 4.1,  "tz": -19.0, "rx": 0, "ry": 90, "rz": 0},
    {"type": "floor", "name": "Floor10", "width": 13.0, "height": 0.5, "depth": 14.0, "tx": -4.5, "ty": 4.5,  "tz": -23.0, "rx": 0, "ry": 90, "rz": 0},

    #FENCES
    {"type": "fence", "name": "Fence1", "width": 6.0,  "height": 1.0, "depth": 1.5, "tx": 9.0,   "ty": 6.0,  "tz": -9.5, "rx": -90, "ry": 0,   "rz": 0},
    {"type": "fence", "name": "Fence2", "width": 10.0, "height": 1.0, "depth": 1.5, "tx": 7.0,   "ty": 6.0,  "tz": 9.5,  "rx": -90, "ry": 0,   "rz": 0},
    {"type": "fence", "name": "Fence3", "width": 18.0, "height": 1.0, "depth": 1.5, "tx": 11.5,  "ty": 6.0,  "tz": 0.0,  "rx": -90, "ry": -90, "rz": 0},
    {"type": "fence", "name": "Fence4", "width": 1.5,  "height": 1.5, "depth": 9.5, "tx": 7.5,   "ty": 1.0,  "tz": -30.0,"rx": 0,   "ry": 90,  "rz": 0},
    {"type": "fence", "name": "Fence5", "width": 1.5,  "height": 1.5, "depth": 6.5, "tx": 11.5,  "ty": 1.0,  "tz": -26.0,"rx": 0,   "ry": 0,   "rz": 0},
    {"type": "fence", "name": "Fence6", "width": 10.0, "height": 1.0, "depth": 3.0, "tx": 5.0,   "ty": 15.0, "tz": -9.5, "rx": -90, "ry": 0,   "rz": 0},

    # ROOFS
    {"type": "roof", "name": "Roof1", "width": 10.0, "height": 1.0, "depth": 20.0, "tx": -5.0, "ty": 23.0, "tz": 0.0,   "rx": 0, "ry": 0, "rz": 0},
    {"type": "roof", "name": "Roof2", "width": 23.0, "height": 1.0, "depth": 14.0, "tx": 0.0,  "ty": 14.0, "tz": -23.5, "rx": 0, "ry": 0, "rz": 0},

    #PILLARS
    {"type": "pillar", "name": "Pillar1", "width": 4.0, "height": 2.0, "depth": 5.0, "tx": -8.0, "ty": 3.0, "tz": 8.0,    "rx": -90, "ry": 0, "rz": 0},
    {"type": "pillar", "name": "Pillar2", "width": 4.0, "height": 2.0, "depth": 5.0, "tx": 8.0,  "ty": 3.0, "tz": 8.0,    "rx": -90, "ry": 0, "rz": 0},
    {"type": "pillar", "name": "Pillar3", "width": 0.5, "height": 4.0, "depth": 0.5, "tx": 20.0, "ty": 6.0, "tz": -16.5,  "rx": 0,   "ry": 0, "rz": 0},
    {"type": "pillar", "name": "Pillar4", "width": 0.5, "height": 4.0, "depth": 0.5, "tx": 20.0, "ty": 6.0, "tz": -20.0,  "rx": 0,   "ry": 0, "rz": 0},
    {"type": "pillar", "name": "Pillar5", "width": 0.5, "height": 4.0, "depth": 0.5, "tx": 20.0, "ty": 8.0, "tz": -18.25, "rx": -90, "ry": 0, "rz": 0},

    #FLOWER BEDS
    {"type": "flowerbed", "name": "FlowerBed1",  "width": 5.0, "height": 6.0, "depth": 5.0,  "tx": 11.5, "ty": 3.5,  "tz": -13.0, "rx": 0, "ry": 0,   "rz": 0},
    {"type": "flowerbed", "name": "FlowerBed2",  "width": 5.0, "height": 4.0, "depth": 6.0,  "tx": 14.0, "ty": 2.5,  "tz": -9.0,  "rx": 0, "ry": 0,   "rz": 0},
    {"type": "flowerbed", "name": "FlowerBed3",  "width": 5.0, "height": 3.0, "depth": 3.0,  "tx": 14.0, "ty": 2.0,  "tz": -5.5,  "rx": 0, "ry": 0,   "rz": 0},
    {"type": "flowerbed", "name": "FlowerBed4",  "width": 5.0, "height": 2.0, "depth": 4.0,  "tx": 14.0, "ty": 1.5,  "tz": -2.0,  "rx": 0, "ry": 0,   "rz": 0},
    {"type": "flowerbed", "name": "FlowerBed5",  "width": 7.0, "height": 1.0, "depth": 2.0,  "tx": 13.0, "ty": 0.74, "tz": 1.0,   "rx": 0, "ry": 0,   "rz": 0},
    {"type": "flowerbed", "name": "FlowerBed6",  "width": 3.0, "height": 5.0, "depth": 4.0,  "tx": 15.0, "ty": 3.0,  "tz": -13.5, "rx": 0, "ry": 0,   "rz": 0},
    {"type": "flowerbed", "name": "FlowerBed7",  "width": 5.0, "height": 4.5, "depth": 13.5, "tx": 23.0, "ty": 2.5,  "tz": -16.0, "rx": 0, "ry": 0,   "rz": 0},
    {"type": "flowerbed", "name": "FlowerBed8",  "width": 5.0, "height": 3.5, "depth": 3.5,  "tx": 23.0, "ty": 2.0,  "tz": -7.5,  "rx": 0, "ry": 0,   "rz": 0},
    {"type": "flowerbed", "name": "FlowerBed9",  "width": 4.5, "height": 2.1, "depth": 5.0,  "tx": 23.0, "ty": 1.3,  "tz": -3.5,  "rx": 0, "ry": 0,   "rz": 0},
    {"type": "flowerbed", "name": "FlowerBed10", "width": 4.5, "height": 1.0, "depth": 2.0,  "tx": 23.0, "ty": 0.75, "tz": 0.0,   "rx": 0, "ry": 0,   "rz": 0},
    {"type": "flowerbed", "name": "FlowerBed11", "width": 3.0, "height": 5.0, "depth": 14.5, "tx": 18.5, "ty": 2.8,  "tz": -23.8, "rx": 0, "ry": 90,  "rz": 0},
    {"type": "flowerbed", "name": "FlowerBed12", "width": 5.0, "height": 3.0, "depth": 13.5, "tx": -5.5, "ty": 2.0,  "tz": 11.0,  "rx": 0, "ry": -90, "rz": 0},
    {"type": "flowerbed", "name": "FlowerBed13", "width": 5.0, "height": 2.0, "depth": 5.0,  "tx": 3.5,  "ty": 1.5,  "tz": 11.0,  "rx": 0, "ry": -90, "rz": 0},

    # STAIRS
    {"type": "stair", "name": "Stair1", "width": 4.5, "height": 0.5, "depth": 1.5, "tx": 18.5, "ty": 0.75, "tz": -0.2, "rx": 0, "ry": 0, "rz": 0},
    {"type": "stair", "name": "Stair2", "width": 4.5, "height": 0.5, "depth": 1.5, "tx": 18.5, "ty": 1.2,  "tz": -1.2, "rx": 0, "ry": 0, "rz": 0},
    {"type": "stair", "name": "Stair3", "width": 4.5, "height": 0.5, "depth": 1.5, "tx": 18.5, "ty": 1.5,  "tz": -2.2, "rx": 0, "ry": 0, "rz": 0},
    {"type": "stair", "name": "Stair4", "width": 4.5, "height": 0.5, "depth": 1.5, "tx": 18.5, "ty": 1.8,  "tz": -3.2, "rx": 0, "ry": 0, "rz": 0},
    {"type": "stair", "name": "Stair5", "width": 4.5, "height": 0.5, "depth": 2.5, "tx": 18.5, "ty": 2.1,  "tz": -5.0, "rx": 0, "ry": 0, "rz": 0},
    {"type": "stair", "name": "Stair6", "width": 4.5, "height": 0.5, "depth": 1.5, "tx": 18.5, "ty": 3.5,  "tz": -9.6, "rx": 0, "ry": 0, "rz": 0},
    {"type": "stair", "name": "Stair7", "width": 4.5, "height": 0.5, "depth": 1.5, "tx": 18.5, "ty": 3.1,  "tz": -8.6, "rx": 0, "ry": 0, "rz": 0},
    {"type": "stair", "name": "Stair8", "width": 4.5, "height": 0.5, "depth": 1.5, "tx": 18.5, "ty": 2.8,  "tz": -7.6, "rx": 0, "ry": 0, "rz": 0},
    {"type": "stair", "name": "Stair9", "width": 4.5, "height": 0.5, "depth": 1.5, "tx": 18.5, "ty": 2.5,  "tz": -6.6, "rx": 0, "ry": 0, "rz": 0},
]


# DISPATCHER
def create_element(entry):
    """
    Route a single config entry to the correct builder function.

    Looks up the entry's 'type' key in the BUILDERS dictionary and calls
    the matching function with the entry's parameters. Unknown types are
    warned and skipped. Exceptions inside builder functions are caught
    so the driver loop always continues.

    Parameters
    ----------
    entry : dict
        A config dictionary with keys: type, name, width, height, depth,
        tx, ty, tz, rx, ry, rz.

    Returns
    -------
    str or None : Maya object name if created, None if skipped or failed.
    """
    element_type = entry.get("type", "unknown")
    builder_fn = BUILDERS.get(element_type)

    if builder_fn is None:
        cmds.warning(f"[core_utils] Unknown type '{element_type}' — skipping.")
        return None

    if DEBUG:
        print(f"[DEBUG] Building '{entry.get('name')}' as type='{element_type}'")

    try:
        result = builder_fn(
            name=entry.get("name", element_type),
            width=entry.get("width", 1.0),
            height=entry.get("height", 1.0),
            depth=entry.get("depth", 1.0),
            tx=entry.get("tx", 0.0),
            ty=entry.get("ty", 0.0),
            tz=entry.get("tz", 0.0),
            rx=entry.get("rx", 0.0),
            ry=entry.get("ry", 0.0),
            rz=entry.get("rz", 0.0),
        )
        if DEBUG and result:
            print(f"[DEBUG] Created: {result}")
        return result

    except Exception as e:
        cmds.warning(f"[core_utils] Failed to build '{entry.get('name')}': {e}")
        return None


# DRIVER LOOP — processes the full CONFIG list
def build_all():
    """
    Iterate over the full CONFIG list and build every element.

    Calls create_element() for each entry. Errors in individual entries
    are caught inside create_element() and do not stop the loop.

    Returns
    -------
    list : Names of all successfully created Maya objects.
    """
    created = []
    for entry in CONFIG:
        result = create_element(entry)
        if result:
            created.append(result)

    print(f"[core_utils] Build complete — {len(created)}/{len(CONFIG)} elements created.")
    return created
