"""
builder.py
----------
Core geometry builder functions for the Modular Modern House Builder tool.
Each function creates a single Maya polyCube primitive with the exact size,
position, and rotation defined from the house layout data.

All functions follow the same signature pattern:
    create_<type>(name, width, height, depth, tx, ty, tz, rx, ry, rz)

Author: [Your Name]
Course: [Course Name]
"""

import maya.cmds as cmds


# ---------------------------------------------------------------------------
# WALL BUILDERS
# ---------------------------------------------------------------------------

def create_wall(name="wall", width=1.0, height=1.0, depth=1.0,
                tx=0.0, ty=0.0, tz=0.0,
                rx=0.0, ry=0.0, rz=0.0):
    """
    Create a wall segment as a polyCube primitive.

    Parameters
    ----------
    name  : str   Display name for the object in the Maya outliner.
    width : float Width of the wall along X axis. Must be > 0.
    height: float Height (thickness) of the wall. Must be > 0.
    depth : float Depth of the wall along Z axis. Must be > 0.
    tx    : float World-space X translation.
    ty    : float World-space Y translation.
    tz    : float World-space Z translation.
    rx    : float X rotation in degrees.
    ry    : float Y rotation in degrees.
    rz    : float Z rotation in degrees.

    Returns
    -------
    str : The name of the created Maya object.
    """
    if width <= 0 or height <= 0 or depth <= 0:
        cmds.warning(f"[builder] '{name}' skipped — size values must be > 0.")
        return None

    obj = cmds.polyCube(w=width, h=height, d=depth, name=name)[0]
    cmds.setAttr(f"{obj}.translateX", tx)
    cmds.setAttr(f"{obj}.translateY", ty)
    cmds.setAttr(f"{obj}.translateZ", tz)
    cmds.setAttr(f"{obj}.rotateX", rx)
    cmds.setAttr(f"{obj}.rotateY", ry)
    cmds.setAttr(f"{obj}.rotateZ", rz)
    return obj


# ---------------------------------------------------------------------------
# FLOOR BUILDERS
# ---------------------------------------------------------------------------

def create_floor(name="floor", width=1.0, height=1.0, depth=1.0,
                 tx=0.0, ty=0.0, tz=0.0,
                 rx=0.0, ry=0.0, rz=0.0):
    """
    Create a floor slab as a polyCube primitive.

    Parameters
    ----------
    name  : str   Display name for the object in the Maya outliner.
    width : float Width of the floor along X axis. Must be > 0.
    height: float Thickness of the floor slab. Must be > 0.
    depth : float Depth of the floor along Z axis. Must be > 0.
    tx    : float World-space X translation.
    ty    : float World-space Y translation.
    tz    : float World-space Z translation.
    rx    : float X rotation in degrees.
    ry    : float Y rotation in degrees.
    rz    : float Z rotation in degrees.

    Returns
    -------
    str : The name of the created Maya object.
    """
    if width <= 0 or height <= 0 or depth <= 0:
        cmds.warning(f"[builder] '{name}' skipped — size values must be > 0.")
        return None

    obj = cmds.polyCube(w=width, h=height, d=depth, name=name)[0]
    cmds.setAttr(f"{obj}.translateX", tx)
    cmds.setAttr(f"{obj}.translateY", ty)
    cmds.setAttr(f"{obj}.translateZ", tz)
    cmds.setAttr(f"{obj}.rotateX", rx)
    cmds.setAttr(f"{obj}.rotateY", ry)
    cmds.setAttr(f"{obj}.rotateZ", rz)
    return obj


# ---------------------------------------------------------------------------
# ROOF BUILDERS
# ---------------------------------------------------------------------------

def create_roof(name="roof", width=1.0, height=1.0, depth=1.0,
                tx=0.0, ty=0.0, tz=0.0,
                rx=0.0, ry=0.0, rz=0.0):
    """
    Create a roof slab as a polyCube primitive.

    Parameters
    ----------
    name  : str   Display name for the object in the Maya outliner.
    width : float Width of the roof panel. Must be > 0.
    height: float Thickness of the roof panel. Must be > 0.
    depth : float Depth of the roof panel. Must be > 0.
    tx    : float World-space X translation.
    ty    : float World-space Y translation.
    tz    : float World-space Z translation.
    rx    : float X rotation in degrees.
    ry    : float Y rotation in degrees.
    rz    : float Z rotation in degrees.

    Returns
    -------
    str : The name of the created Maya object.
    """
    if width <= 0 or height <= 0 or depth <= 0:
        cmds.warning(f"[builder] '{name}' skipped — size values must be > 0.")
        return None

    obj = cmds.polyCube(w=width, h=height, d=depth, name=name)[0]
    cmds.setAttr(f"{obj}.translateX", tx)
    cmds.setAttr(f"{obj}.translateY", ty)
    cmds.setAttr(f"{obj}.translateZ", tz)
    cmds.setAttr(f"{obj}.rotateX", rx)
    cmds.setAttr(f"{obj}.rotateY", ry)
    cmds.setAttr(f"{obj}.rotateZ", rz)
    return obj


# ---------------------------------------------------------------------------
# FENCE BUILDERS
# ---------------------------------------------------------------------------

def create_fence(name="fence", width=1.0, height=1.0, depth=1.0,
                 tx=0.0, ty=0.0, tz=0.0,
                 rx=0.0, ry=0.0, rz=0.0):
    """
    Create a fence panel as a polyCube primitive.

    Parameters
    ----------
    name  : str   Display name for the object in the Maya outliner.
    width : float Width of the fence panel. Must be > 0.
    height: float Height of the fence panel. Must be > 0.
    depth : float Depth (thickness) of the fence panel. Must be > 0.
    tx    : float World-space X translation.
    ty    : float World-space Y translation.
    tz    : float World-space Z translation.
    rx    : float X rotation in degrees.
    ry    : float Y rotation in degrees.
    rz    : float Z rotation in degrees.

    Returns
    -------
    str : The name of the created Maya object.
    """
    if width <= 0 or height <= 0 or depth <= 0:
        cmds.warning(f"[builder] '{name}' skipped — size values must be > 0.")
        return None

    obj = cmds.polyCube(w=width, h=height, d=depth, name=name)[0]
    cmds.setAttr(f"{obj}.translateX", tx)
    cmds.setAttr(f"{obj}.translateY", ty)
    cmds.setAttr(f"{obj}.translateZ", tz)
    cmds.setAttr(f"{obj}.rotateX", rx)
    cmds.setAttr(f"{obj}.rotateY", ry)
    cmds.setAttr(f"{obj}.rotateZ", rz)
    return obj


# ---------------------------------------------------------------------------
# PILLAR BUILDERS
# ---------------------------------------------------------------------------

def create_pillar(name="pillar", width=1.0, height=1.0, depth=1.0,
                  tx=0.0, ty=0.0, tz=0.0,
                  rx=0.0, ry=0.0, rz=0.0):
    """
    Create a structural pillar as a polyCube primitive.

    Parameters
    ----------
    name  : str   Display name for the object in the Maya outliner.
    width : float Width of the pillar. Must be > 0.
    height: float Height of the pillar. Must be > 0.
    depth : float Depth of the pillar. Must be > 0.
    tx    : float World-space X translation.
    ty    : float World-space Y translation.
    tz    : float World-space Z translation.
    rx    : float X rotation in degrees.
    ry    : float Y rotation in degrees.
    rz    : float Z rotation in degrees.

    Returns
    -------
    str : The name of the created Maya object.
    """
    if width <= 0 or height <= 0 or depth <= 0:
        cmds.warning(f"[builder] '{name}' skipped — size values must be > 0.")
        return None

    obj = cmds.polyCube(w=width, h=height, d=depth, name=name)[0]
    cmds.setAttr(f"{obj}.translateX", tx)
    cmds.setAttr(f"{obj}.translateY", ty)
    cmds.setAttr(f"{obj}.translateZ", tz)
    cmds.setAttr(f"{obj}.rotateX", rx)
    cmds.setAttr(f"{obj}.rotateY", ry)
    cmds.setAttr(f"{obj}.rotateZ", rz)
    return obj


# ---------------------------------------------------------------------------
# FLOWER BED BUILDERS
# ---------------------------------------------------------------------------

def create_flower_bed(name="flowerbed", width=1.0, height=1.0, depth=1.0,
                      tx=0.0, ty=0.0, tz=0.0,
                      rx=0.0, ry=0.0, rz=0.0):
    """
    Create a landscaping flower bed volume as a polyCube primitive.

    Parameters
    ----------
    name  : str   Display name for the object in the Maya outliner.
    width : float Width of the flower bed. Must be > 0.
    height: float Height of the flower bed mound. Must be > 0.
    depth : float Depth of the flower bed. Must be > 0.
    tx    : float World-space X translation.
    ty    : float World-space Y translation.
    tz    : float World-space Z translation.
    rx    : float X rotation in degrees.
    ry    : float Y rotation in degrees.
    rz    : float Z rotation in degrees.

    Returns
    -------
    str : The name of the created Maya object.
    """
    if width <= 0 or height <= 0 or depth <= 0:
        cmds.warning(f"[builder] '{name}' skipped — size values must be > 0.")
        return None

    obj = cmds.polyCube(w=width, h=height, d=depth, name=name)[0]
    cmds.setAttr(f"{obj}.translateX", tx)
    cmds.setAttr(f"{obj}.translateY", ty)
    cmds.setAttr(f"{obj}.translateZ", tz)
    cmds.setAttr(f"{obj}.rotateX", rx)
    cmds.setAttr(f"{obj}.rotateY", ry)
    cmds.setAttr(f"{obj}.rotateZ", rz)
    return obj


# ---------------------------------------------------------------------------
# STAIR BUILDERS
# ---------------------------------------------------------------------------

def create_stair(name="stair", width=1.0, height=1.0, depth=1.0,
                 tx=0.0, ty=0.0, tz=0.0,
                 rx=0.0, ry=0.0, rz=0.0):
    """
    Create a single stair step as a polyCube primitive.

    Parameters
    ----------
    name  : str   Display name for the object in the Maya outliner.
    width : float Width of the stair step. Must be > 0.
    height: float Riser height of the step. Must be > 0.
    depth : float Tread depth of the step. Must be > 0.
    tx    : float World-space X translation.
    ty    : float World-space Y translation.
    tz    : float World-space Z translation.
    rx    : float X rotation in degrees.
    ry    : float Y rotation in degrees.
    rz    : float Z rotation in degrees.

    Returns
    -------
    str : The name of the created Maya object.
    """
    if width <= 0 or height <= 0 or depth <= 0:
        cmds.warning(f"[builder] '{name}' skipped — size values must be > 0.")
        return None

    obj = cmds.polyCube(w=width, h=height, d=depth, name=name)[0]
    cmds.setAttr(f"{obj}.translateX", tx)
    cmds.setAttr(f"{obj}.translateY", ty)
    cmds.setAttr(f"{obj}.translateZ", tz)
    cmds.setAttr(f"{obj}.rotateX", rx)
    cmds.setAttr(f"{obj}.rotateY", ry)
    cmds.setAttr(f"{obj}.rotateZ", rz)
    return obj
