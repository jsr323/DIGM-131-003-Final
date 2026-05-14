# DIGM-131-003-Final
A Maya Python tool for assembling modular modern house environments  using a custom UI.

maya-house-builder/
- main.py              # Entry point, sys.path, self-test
- ui.py                # Maya UI window
- builder.py           # Core placement and transform functions
- pieces.py            # Piece definitions and mesh creation
- scene_manager.py     # Save/load layout via JSON
- validator.py         # Input validation and error handling

README.md

Planned Functions
- Place_piece(name, x, y, z) - Places a piece at a grid coordinate
- snap_to_grid(obj, grid_size) - Snaps object to nearest grid unit
- randomize_color(obj) - Assigns a random material color
- Save_layout(filepath) - Exports current scene layout to JSON
- load_layout(filepath) - Rebuilds a scene from a saved JSON file
- Validate_position(x, y, z) - Checks for out of bounds or overlapping
