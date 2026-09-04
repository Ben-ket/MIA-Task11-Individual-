# Camera-to-Base Frame Transformation (Task 11.2)

Quick Python script to convert 3D coordinates detected by a front-facing camera (`camera_link`) into the vehicle's center frame (`base_link`).

## What it does

The front camera on the race car detects obstacles relative to its own focal point. To help the vehicle make steering and driving decisions, coordinates need to be transformed into the vehicle's base frame (`base_link`).

This script applies:
1. **Pitch Rotation (Y-axis)**: Tilts the coordinates by -15 degrees around the Y-axis.
2. **Translation**: Adds the camera mounting offset `(tx=0.5m, ty=0.0m, tz=0.2m)`.


## Usage

Simply run the script with Python:

```bash
python Camera-to-Base.py
