from vpython import (
    arrow,
    color,
    degrees,
    diff_angle,
    label,
    scene,
    sphere,
    vector,
)

# --- 1. Define Bond Vectors (C-H) ---
A = vector(1, 1, 1)
B = vector(1, -1, -1)
C = vector(-1, 1, -1)
D = vector(-1, -1, 1)

# Calculate angle between A and B
bond_angle_deg = degrees(diff_angle(A, B))

# --- 2. 3D Scene Setup ---
scene.title = "3D Molecular Geometry: CH4 Bond Angle (Problem 1.74)"
scene.background = color.white
scene.center = vector(0, 0, 0)
scene.range = 2.5

# --- 3. Light Gray Reference Coordinate Axes ---
axis_len = 1.8
axis_color = color.gray(0.85)  # Light gray

# X-axis (+X / -X)
arrow(
    pos=vector(-axis_len, 0, 0),
    axis=vector(2 * axis_len, 0, 0),
    color=axis_color,
    shaftwidth=0.015,
    headwidth=0.04,
)
label(
    pos=vector(axis_len + 0.1, 0, 0),
    text="+X",
    color=axis_color,
    box=False,
    opacity=0,
    height=10,
)

# Y-axis (+Y / -Y)
arrow(
    pos=vector(0, -axis_len, 0),
    axis=vector(0, 2 * axis_len, 0),
    color=axis_color,
    shaftwidth=0.015,
    headwidth=0.04,
)
label(
    pos=vector(0, axis_len + 0.1, 0),
    text="+Y",
    color=axis_color,
    box=False,
    opacity=0,
    height=10,
)

# Z-axis (+Z / -Z)
arrow(
    pos=vector(0, 0, -axis_len),
    axis=vector(0, 0, 2 * axis_len),
    color=axis_color,
    shaftwidth=0.015,
    headwidth=0.04,
)
label(
    pos=vector(0, 0, axis_len + 0.1),
    text="+Z",
    color=axis_color,
    box=False,
    opacity=0,
    height=10,
)

# --- 4. Draw Atoms ---
sphere(pos=vector(0, 0, 0), radius=0.35, color=color.gray(0.3))  # Central Carbon

h_radius = 0.20
sphere(pos=A, radius=h_radius, color=color.cyan)
sphere(pos=B, radius=h_radius, color=color.cyan)
sphere(pos=C, radius=h_radius, color=color.gray(0.7))
sphere(pos=D, radius=h_radius, color=color.gray(0.7))

# --- 5. Draw Bond Vectors ---
arrow(pos=vector(0, 0, 0), axis=A, color=color.blue, shaftwidth=0.08)
arrow(pos=vector(0, 0, 0), axis=B, color=color.red, shaftwidth=0.08)
arrow(pos=vector(0, 0, 0), axis=C, color=color.gray(0.6), shaftwidth=0.04)
arrow(pos=vector(0, 0, 0), axis=D, color=color.gray(0.6), shaftwidth=0.04)

# --- 6. Add Labels ---
label(
    pos=A,
    text="H1 (i + j + k)",
    xoffset=20,
    yoffset=20,
    color=color.blue,
    height=12,
    box=True,
)
label(
    pos=B,
    text="H2 (i - j - k)",
    xoffset=20,
    yoffset=-20,
    color=color.red,
    height=12,
    box=True,
)
label(
    pos=vector(0, 0, 0),
    text=f"Carbon Center\nBond Angle: {bond_angle_deg:.1f}°",
    xoffset=-50,
    yoffset=-40,
    color=color.black,
    height=12,
    box=True,
)

scene.waitfor("click")
