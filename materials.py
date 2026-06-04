
"""
materials.py
------------
Material creation and assignment functions for the Modular Modern House
Builder tool. Creates Arnold aiStandardSurface materials and applies them
to the correct PolyCube objects in the scene.

Materials
---------
- Cream_Concrete: Warm off-white concrete (HSV 40, 0.2, 0.5)
- Glass: Semi-transparent glass (transmission 0.8)
- Grass_FlowerBed: Muted green vegetation (HSV 100, 0.3, 0.3)
Author: Jillian Richards
Course: DIGM 131
"""

import colorsys
import maya.cmds as cmds


# DEBUG FLAG — mirrors the flag in core_utils.py
DEBUG = True


# HELPER FUNCTIONS
def hsv_to_rgb(h, s, v):
    """
    Convert HSV color values to RGB for use in Maya shader attributes.

    Maya's color attributes expect RGB values in the 0.0 - 1.0 range.
    HSV input uses the same 0.0 - 1.0 range (hue is 0-360 divided by 360).

    Parameters
    ----------
    h : float  Hue in degrees (0 - 360).
    s : float  Saturation (0.0 - 1.0).
    v : float  Value / brightness (0.0 - 1.0).

    Returns
    -------
    tuple : (r, g, b) each in 0.0 - 1.0 range.
    """
    r, g, b = colorsys.hsv_to_rgb(h / 360.0, s, v)
    return r, g, b


def assign_material(material_name, objects):
    """
    Assign an existing material to a list of Maya objects by name.

    Looks up the shading group connected to the material and uses
    cmds.sets() to assign it. Issues a warning for any object that
    does not exist in the scene.

    Parameters
    ----------
    material_name : str   Name of the Maya material node to assign.
    objects       : list  List of Maya object name strings.

    Returns
    -------
    None
    """
    # Find the shading group connected to this material
    shading_groups = cmds.listConnections(
        material_name, type="shadingEngine"
    )

    if not shading_groups:
        cmds.warning(
            f"[materials] No shading group found for '{material_name}'. "
            "Cannot assign material."
        )
        return

    sg = shading_groups[0]

    for obj in objects:
        if not cmds.objExists(obj):
            cmds.warning(
                f"[materials] Object '{obj}' not found in scene — skipping."
            )
            continue
        try:
            cmds.sets(obj, edit=True, forceElement=sg)
            if DEBUG:
                print(f"[DEBUG] Assigned '{material_name}' to '{obj}'")
        except Exception as e:
            cmds.warning(
                f"[materials] Failed to assign '{material_name}' "
                f"to '{obj}': {e}"
            )


# MATERIAL 1 — Cream_Concrete
# HSV: H=40, S=0.2, V=0.5  →  warm off-white concrete
# ---------------------------------------------------------------------------

# Objects that receive the Cream_Concrete material
CREAM_CONCRETE_OBJECTS = [
    "Wall1", "Wall2", "Wall6", "Wall7", "Wall9", "Wall10",
    "Wall11", "Wall12", "Wall13", "Wall14", "Wall15", "Wall16",
    "Floor1", "Floor2", "Floor3", "Floor4", "Floor5", "Floor6",
    "Floor7", "Floor8", "Floor9", "Floor10",
    "Fence1", "Fence2", "Fence3", "Fence4", "Fence5", "Fence6",
    "Roof1", "Roof2",
    "Pillar1", "Pillar2",
    "Stair1", "Stair2", "Stair3", "Stair4", "Stair5",
    "Stair6", "Stair7", "Stair8", "Stair9",
]


def create_cream_concrete():
    """
    Create the Cream_Concrete Arnold aiStandardSurface material.

    Color is defined in HSV (H=40, S=0.2, V=0.5) and converted to RGB
    before being applied to the shader's base color attribute.
    Assigns the material to all objects in CREAM_CONCRETE_OBJECTS.

    Returns
    -------
    str or None : Name of the created material node, or None if failed.
    """
    material_name = "Cream_Concrete"

    try:
        # Convert HSV to RGB
        r, g, b = hsv_to_rgb(h=40, s=0.2, v=0.5)

        if DEBUG:
            print(
                f"[DEBUG] Cream_Concrete RGB: "
                f"R={r:.4f}  G={g:.4f}  B={b:.4f}"
            )

        # Create aiStandardSurface shader and shading group
        material = cmds.shadingNode(
            "aiStandardSurface",
            asShader=True,
            name=material_name
        )
        shading_group = cmds.sets(
            renderable=True,
            noSurfaceShader=True,
            empty=True,
            name=f"{material_name}SG"
        )

        # Connect shader to shading group
        cmds.connectAttr(
            f"{material}.outColor",
            f"{shading_group}.surfaceShader",
            force=True
        )

        # Set base color
        cmds.setAttr(f"{material}.baseColor", r, g, b, type="double3")

        if DEBUG:
            print(f"[DEBUG] Created material: {material}")

        # Assign to objects
        assign_material(material_name, CREAM_CONCRETE_OBJECTS)

        return material

    except Exception as e:
        cmds.warning(f"[materials] Failed to create Cream_Concrete: {e}")
        return None


# MATERIAL 2 — Glass
# Transmission: 0.8  →  semi-transparent glass panels
# ---------------------------------------------------------------------------

# Objects that receive the Glass material
GLASS_OBJECTS = [
    "Wall3", "Wall4", "Wall5", "Wall8",
    "Pillar3", "Pillar4", "Pillar5",
]


def create_glass():
    """
    Create the Glass Arnold aiStandardSurface material.

    Sets transmission to 0.8 to achieve a semi-transparent glass look.
    Assigns the material to all objects in GLASS_OBJECTS.

    Returns
    -------
    str or None : Name of the created material node, or None if failed.
    """
    material_name = "Glass"

    try:
        # Create aiStandardSurface shader and shading group
        material = cmds.shadingNode(
            "aiStandardSurface",
            asShader=True,
            name=material_name
        )
        shading_group = cmds.sets(
            renderable=True,
            noSurfaceShader=True,
            empty=True,
            name=f"{material_name}SG"
        )

        # Connect shader to shading group
        cmds.connectAttr(
            f"{material}.outColor",
            f"{shading_group}.surfaceShader",
            force=True
        )

        # Set transmission for glass effect
        cmds.setAttr(f"{material}.transmission", 0.8)

        if DEBUG:
            print(f"[DEBUG] Created material: {material}")
            print(f"[DEBUG] Glass transmission set to 0.8")

        # Assign to objects
        assign_material(material_name, GLASS_OBJECTS)

        return material

    except Exception as e:
        cmds.warning(f"[materials] Failed to create Glass: {e}")
        return None


# MATERIAL 3 — Grass_FlowerBed
# HSV: H=100, S=0.3, V=0.3  →  muted dark green vegetation
# ---------------------------------------------------------------------------

# Objects that receive the Grass_FlowerBed material
GRASS_FLOWERBED_OBJECTS = [
    "FlowerBed1", "FlowerBed2", "FlowerBed3", "FlowerBed4",
    "FlowerBed5", "FlowerBed6", "FlowerBed7", "FlowerBed8",
    "FlowerBed9", "FlowerBed10", "FlowerBed11", "FlowerBed12",
    "FlowerBed13",
]


def create_grass_flowerbed():
    """
    Create the Grass_FlowerBed Arnold aiStandardSurface material.

    Color is defined in HSV (H=100, S=0.3, V=0.3) and converted to RGB
    before being applied to the shader's base color attribute.
    Assigns the material to all objects in GRASS_FLOWERBED_OBJECTS.

    Returns
    -------
    str or None : Name of the created material node, or None if failed.
    """
    material_name = "Grass_FlowerBed"

    try:
        # Convert HSV to RGB
        r, g, b = hsv_to_rgb(h=100, s=0.3, v=0.3)

        if DEBUG:
            print(
                f"[DEBUG] Grass_FlowerBed RGB: "
                f"R={r:.4f}  G={g:.4f}  B={b:.4f}"
            )

        # Create aiStandardSurface shader and shading group
        material = cmds.shadingNode(
            "aiStandardSurface",
            asShader=True,
            name=material_name
        )
        shading_group = cmds.sets(
            renderable=True,
            noSurfaceShader=True,
            empty=True,
            name=f"{material_name}SG"
        )

        # Connect shader to shading group
        cmds.connectAttr(
            f"{material}.outColor",
            f"{shading_group}.surfaceShader",
            force=True
        )

        # Set base color
        cmds.setAttr(f"{material}.baseColor", r, g, b, type="double3")

        if DEBUG:
            print(f"[DEBUG] Created material: {material}")

        # Assign to objects
        assign_material(material_name, GRASS_FLOWERBED_OBJECTS)

        return material

    except Exception as e:
        cmds.warning(f"[materials] Failed to create Grass_FlowerBed: {e}")
        return None


# DRIVER — create and assign all three materials at once
def build_all_materials():
    """
    Create and assign all three house materials in sequence.

    Calls create_cream_concrete(), create_glass(), and
    create_grass_flowerbed(). Each function handles its own
    error handling and object assignment internally.

    Returns
    -------
    dict : Keys are material names, values are created node names or None.
    """
    print("[materials] Building all materials...")

    results = {
        "Cream_Concrete":  create_cream_concrete(),
        "Glass":           create_glass(),
        "Grass_FlowerBed": create_grass_flowerbed(),
    }

    created = [k for k, v in results.items() if v is not None]
    print(
        f"[materials] Done — "
        f"{len(created)}/3 materials created and assigned."
    )

    return results
