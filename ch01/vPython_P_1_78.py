import numpy as np
from vpython import arrow, color, label, scene, sphere, vector

# --- Physical Parameters ---
r_mag = 4.0  # m
F_mag = 22.0  # N
theta_deg = 36.0  # deg from +y to -x

# Position vector r
rx = -r_mag * np.sin(np.radians(theta_deg))
ry = r_mag * np.cos(np.radians(theta_deg))
r_vec = vector(rx, ry, 0)

# Force vector F
F_vec = vector(0, -F_mag, 0)

# Torque tau = r x F
tau_vec = r_vec.cross(F_vec)

# --- Visual Scales ---
scale_F = 0.12  # Scale force vector for display
scale_tau = 0.08  # Scale torque vector for display

# --- 3D Scene Setup ---
scene.title = "3D Vector Visualization: Torque τ = r × F (Problem 1.78)"
scene.background = color.white
scene.center = vector(-1.0, 1.5, 1.5)
scene.range = 5.5

# Light Gray Reference Axes
axis_len = 4.5
axis_col = color.gray(0.85)

arrow(
    pos=vector(-axis_len, 0, 0),
    axis=vector(2 * axis_len, 0, 0),
    color=axis_col,
    shaftwidth=0.03,
)  # X-axis
arrow(
    pos=vector(0, -axis_len, 0),
    axis=vector(0, 2 * axis_len, 0),
    color=axis_col,
    shaftwidth=0.03,
)  # Y-axis
arrow(
    pos=vector(0, 0, -axis_len),
    axis=vector(0, 0, 2 * axis_len),
    color=axis_col,
    shaftwidth=0.03,
)  # Z-axis

# Axis of Rotation (Origin)
sphere(pos=vector(0, 0, 0), radius=0.15, color=color.black)

# Position Vector r (Blue)
arrow(pos=vector(0, 0, 0), axis=r_vec, color=color.blue, shaftwidth=0.10)

# Force Vector F applied at tip of r (Red)
arrow(pos=r_vec, axis=F_vec * scale_F, color=color.red, shaftwidth=0.10)

# Torque Vector tau at origin along +z (Green)
arrow(
    pos=vector(0, 0, 0),
    axis=tau_vec * scale_tau,
    color=color.green,
    shaftwidth=0.10,
)

# --- Labels ---
label(
    pos=vector(0, 0, 0),
    text="Axis of Rotation",
    xoffset=-40,
    yoffset=-40,
    color=color.black,
    height=12,
    box=True,
)

label(
    pos=r_vec,
    text=f"Position r = {r_mag:.1f} m\n(36° from +y to -x)",
    xoffset=-30,
    yoffset=30,
    color=color.blue,
    height=12,
    box=True,
)

label(
    pos=r_vec + F_vec * scale_F,
    text=f"Force F = {F_mag:.1f} N (-y)",
    xoffset=-30,
    yoffset=-20,
    color=color.red,
    height=12,
    box=True,
)

label(
    pos=tau_vec * scale_tau,
    text=f"Torque τ = {tau_vec.z:.1f} N·m (+z)",
    xoffset=30,
    yoffset=20,
    color=color.green,
    height=12,
    box=True,
)

scene.waitfor("click")
