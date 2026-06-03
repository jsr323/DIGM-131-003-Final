"""
ui.py
-----
Custom Maya UI window for the Modular Modern House Builder tool.
Provides a panel with piece-type buttons, X/Y/Z position fields,
size fields, and a Build button that calls the actual builder
functions from builder.py via the BUILDERS dispatcher in core_utils.py.

How to open:
    Run main.py in the Maya Script Editor, or call open_house_builder_ui()
    directly from the Script Editor after importing ui.py.

Author: Jillian Richards
Course: DIGM131
"""

import maya.cmds as cmds
from core_utils import BUILDERS, DEBUG

# WINDOW CONSTANTS
WINDOW_ID = "houseBuilderWindow"
WINDOW_TITLE = "Modular House Builder"

# Piece types available in the UI — matches BUILDERS dict keys
PIECE_TYPES = ["wall", "floor", "roof", "fence", "pillar", "flowerbed", "stair"]

# Stores the currently selected piece type
_selected_type = {"value": "wall"}

# FIELD REFERENCES — used to read input values when Build is clicked
_fields = {}


# UI HELPER FUNCTIONS
def _set_type(piece_type):
    """
    Set the currently selected piece type when a type button is clicked.

    Updates the internal _selected_type tracker and refreshes the
    label showing the active selection.

    Parameters
    ----------
    piece_type : str  The piece type string (e.g. 'wall', 'floor').

    Returns
    -------
    None
    """
    _selected_type["value"] = piece_type
    if cmds.text("selectedTypeLabel", exists=True):
        cmds.text("selectedTypeLabel", edit=True,
                  label=f"Selected:  {piece_type.upper()}")
    if DEBUG:
        print(f"[DEBUG] UI piece type set to: {piece_type}")


def _get_float(field_key, default=0.0):
    """
    Safely read a float value from a named UI float field.

    Returns the default value and issues a warning if the field
    does not exist or the value cannot be read.

    Parameters
    ----------
    field_key : str   Key name in the _fields dictionary.
    default   : float Fallback value if the read fails.

    Returns
    -------
    float : Value from the field, or the default on failure.
    """
    try:
        return cmds.floatField(_fields[field_key], query=True, value=True)
    except Exception as e:
        cmds.warning(f"[ui] Could not read field '{field_key}': {e}")
        return default


def _validate_size(width, height, depth, name):
    """
    Validate that all three size values are greater than zero.

    Issues a Maya warning and returns False if any value is
    zero or negative, so the build is safely aborted before
    passing bad data to the builder function.

    Parameters
    ----------
    width  : float  Width value to validate.
    height : float  Height value to validate.
    depth  : float  Depth value to validate.
    name   : str    Piece name used in the warning message.

    Returns
    -------
    bool : True if all values are valid, False otherwise.
    """
    if width <= 0 or height <= 0 or depth <= 0:
        cmds.warning(
            f"[ui] '{name}' — width, height, and depth must all be > 0. "
            "Build cancelled."
        )
        return False
    return True


# BUILD CALLBACK — called when the Build button is clicked
def _on_build_clicked(*args):
    """
    Read all UI field values and call the appropriate builder function.

    Reads the selected piece type, name, size (width/height/depth), and
    position (tx/ty/tz) from the UI fields. Validates size inputs, then
    uses the BUILDERS dispatcher dict to call the correct builder function
    with ** unpacking.

    Parameters
    ----------
    *args : Ignored. Maya passes button state as an extra argument.

    Returns
    -------
    None
    """
    piece_type = _selected_type["value"]
    builder_fn = BUILDERS.get(piece_type)

    if builder_fn is None:
        cmds.warning(f"[ui] No builder found for type '{piece_type}'.")
        return

    # Read name from text field
    try:
        name = cmds.textField(_fields["name"], query=True, text=True).strip()
        if not name:
            name = piece_type
    except Exception:
        name = piece_type

    # Read size and position fields
    width  = _get_float("width",  default=1.0)
    height = _get_float("height", default=1.0)
    depth  = _get_float("depth",  default=1.0)
    tx     = _get_float("tx",     default=0.0)
    ty     = _get_float("ty",     default=0.0)
    tz     = _get_float("tz",     default=0.0)

    # Validate before building
    if not _validate_size(width, height, depth, name):
        return

    # Build using ** unpacking into the builder function
    params = {
        "name":   name,
        "width":  width,
        "height": height,
        "depth":  depth,
        "tx":     tx,
        "ty":     ty,
        "tz":     tz,
    }

    if DEBUG:
        print(f"[DEBUG] UI building: type={piece_type}  params={params}")

    try:
        result = builder_fn(**params)
        if result:
            cmds.warning(f"[ui] Built '{result}' successfully.")
        else:
            cmds.warning(f"[ui] Build returned None — check size values.")
    except Exception as e:
        cmds.warning(f"[ui] Build failed for '{name}': {e}")


def _on_clear_clicked(*args):
    """
    Delete all objects in the Maya scene created by the house builder.

    Searches for all polygon mesh objects in the scene and deletes them.
    Prompts a confirmation warning before clearing.

    Parameters
    ----------
    *args : Ignored.

    Returns
    -------
    None
    """
    try:
        all_meshes = cmds.ls(type="mesh")
        if not all_meshes:
            cmds.warning("[ui] No mesh objects found in scene.")
            return
        transforms = cmds.listRelatives(all_meshes, parent=True) or []
        if transforms:
            cmds.delete(transforms)
            cmds.warning(f"[ui] Cleared {len(transforms)} objects from scene.")
        if DEBUG:
            print(f"[DEBUG] Cleared objects: {transforms}")
    except Exception as e:
        cmds.warning(f"[ui] Clear scene failed: {e}")


# UI LAYOUT BUILDER
def open_house_builder_ui():
    """
    Create and display the Modular House Builder Maya UI window.

    Closes any existing instance of the window before rebuilding it.
    Creates a layout with piece-type selector buttons, name/size/position
    input fields, a Build button, and a Clear Scene button.

    Returns
    -------
    str : The name of the Maya window object created.
    """
    # Close existing window if open
    if cmds.window(WINDOW_ID, exists=True):
        cmds.deleteUI(WINDOW_ID)

    # Create the window
    window = cmds.window(
        WINDOW_ID,
        title=WINDOW_TITLE,
        widthHeight=(340, 520),
        sizeable=False
    )

    # Main column layout
    cmds.columnLayout(adjustableColumn=True, rowSpacing=6, columnOffset=("both", 10))

    # ── Title ──────────────────────────────────────────────────────────────
    cmds.separator(height=8, style="none")
    cmds.text(label="MODULAR HOUSE BUILDER", font="boldLabelFont", height=22)
    cmds.separator(height=4, style="in")

    # ── Piece Type Selector ────────────────────────────────────────────────
    cmds.text(label="Select Piece Type:", align="left")
    cmds.separator(height=4, style="none")

    # Two rows of type buttons
    row1_types = ["wall", "floor", "roof", "fence"]
    row2_types = ["pillar", "flowerbed", "stair"]

    cmds.rowLayout(numberOfColumns=len(row1_types),
                   columnWidth4=(75, 75, 75, 75))
    for pt in row1_types:
        cmds.button(
            label=pt.capitalize(),
            width=75,
            command=lambda _, t=pt: _set_type(t)
        )
    cmds.setParent("..")

    cmds.rowLayout(numberOfColumns=len(row2_types),
                   columnWidth3=(75, 75, 75))
    for pt in row2_types:
        cmds.button(
            label=pt.capitalize(),
            width=75,
            command=lambda _, t=pt: _set_type(t)
        )
    cmds.setParent("..")

    # Active type display label
    cmds.separator(height=4, style="none")
    cmds.text("selectedTypeLabel", label="Selected:  WALL",
              font="boldLabelFont", align="left")

    cmds.separator(height=6, style="in")

    # ── Name Field ─────────────────────────────────────────────────────────
    cmds.text(label="Object Name:", align="left")
    _fields["name"] = cmds.textField(placeholderText="e.g. Wall1")

    cmds.separator(height=6, style="in")

    # ── Size Fields ────────────────────────────────────────────────────────
    cmds.text(label="Size  (Width / Height / Depth):", align="left")
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(95, 95, 95))
    _fields["width"]  = cmds.floatField(value=1.0, minValue=0.001,
                                         precision=2, width=95)
    _fields["height"] = cmds.floatField(value=1.0, minValue=0.001,
                                         precision=2, width=95)
    _fields["depth"]  = cmds.floatField(value=1.0, minValue=0.001,
                                         precision=2, width=95)
    cmds.setParent("..")

    # Size axis labels
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(95, 95, 95))
    cmds.text(label="  Width",  align="center", width=95, font="smallBoldLabelFont")
    cmds.text(label="  Height", align="center", width=95, font="smallBoldLabelFont")
    cmds.text(label="  Depth",  align="center", width=95, font="smallBoldLabelFont")
    cmds.setParent("..")

    cmds.separator(height=6, style="in")

    # ── Position Fields ────────────────────────────────────────────────────
    cmds.text(label="Position  (X / Y / Z):", align="left")
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(95, 95, 95))
    _fields["tx"] = cmds.floatField(value=0.0, precision=2, width=95)
    _fields["ty"] = cmds.floatField(value=0.0, precision=2, width=95)
    _fields["tz"] = cmds.floatField(value=0.0, precision=2, width=95)
    cmds.setParent("..")

    # Position axis labels
    cmds.rowLayout(numberOfColumns=3, columnWidth3=(95, 95, 95))
    cmds.text(label="  X", align="center", width=95, font="smallBoldLabelFont")
    cmds.text(label="  Y", align="center", width=95, font="smallBoldLabelFont")
    cmds.text(label="  Z", align="center", width=95, font="smallBoldLabelFont")
    cmds.setParent("..")

    cmds.separator(height=10, style="in")

    # ── Action Buttons ─────────────────────────────────────────────────────
    cmds.button(
        label="BUILD PIECE",
        height=40,
        backgroundColor=(0.2, 0.6, 0.3),
        command=_on_build_clicked
    )
    cmds.separator(height=4, style="none")
    cmds.button(
        label="Clear Scene",
        height=28,
        backgroundColor=(0.6, 0.2, 0.2),
        command=_on_clear_clicked
    )

    cmds.separator(height=8, style="none")

    # Show the window
    cmds.showWindow(window)

    if DEBUG:
        print(f"[DEBUG] UI window opened: {WINDOW_ID}")

    return window
