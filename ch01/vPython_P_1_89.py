import numpy as np
from vpython import arrow, color, label, ring, scene, sphere, vector

# --- Physical Coordinates (AU) ---
r_Sun = vector(0, 0, 0)
r_Earth = vector(0.3182, 0.9329, 0.0000)
r_Mars = vector(1.3087, -0.4423, -0.0414)

# Calculations
r_SE = r_Earth.mag
r_SM = r_Mars.mag
r_EM_vec = r_Mars - r_Earth
r_EM = r_EM_vec.mag

u_ES = -r_Earth
theta_rad = np.arccos(u_ES.dot(r_EM_vec) / (r_SE * r_EM))
theta_deg = np.degrees(theta_rad)

# --- 3D Scene Setup ---
scene.title = "Solar System Navigation: Earth & Mars Positions (Problem 1.89)"
scene.background = color.white
scene.center = vector(0.6, 0.2, 0.0)
scene.range = 2.2

# Light Gray Reference Coordinate Axes
axis_len = 1.8
axis_col = color.gray(0.85)

arrow(
    pos=vector(-axis_len, 0, 0),
    axis=vector(2 * axis_len, 0, 0),
    color=axis_col,
    shaftwidth=0.015,
)  # X-axis
arrow(
    pos=vector(0, -axis_len, 0),
    axis=vector(0, 2 * axis_len, 0),
    color=axis_col,
    shaftwidth=0.015,
)  # Y-axis
arrow(
    pos=vector(0, 0, -axis_len),
    axis=vector(0, 0, 2 * axis_len),
    color=axis_col,
    shaftwidth=0.015,
)  # Z-axis

# Orbit Lines (Reference Rings)
ring(
    pos=r_Sun,
    axis=vector(0, 0, 1),
    radius=r_SE,
    thickness=0.005,
    color=color.gray(0.8),
)
ring(
    pos=r_Sun,
    axis=vector(0, 0, 1),
    radius=r_SM,
    thickness=0.005,
    color=color.gray(0.8),
)

# Celestial Bodies
sphere(pos=r_Sun, radius=0.12, color=color.yellow)  # Sun
sphere(pos=r_Earth, radius=0.06, color=color.blue)  # Earth
sphere(pos=r_Mars, radius=0.05, color=color.red)  # Mars

# Connecting Vectors
arrow(
    pos=r_Sun,
    axis=r_Earth,
    color=color.blue,
    shaftwidth=0.02,
    opacity=0.5,
)  # Sun to Earth
arrow(
    pos=r_Sun,
    axis=r_Mars,
    color=color.red,
    shaftwidth=0.02,
    opacity=0.5,
)  # Sun to Mars
arrow(pos=r_Earth, axis=r_EM_vec, color=color.orange, shaftwidth=0.025)  # Earth to Mars

# --- Labels ---
label(
    pos=r_Sun,
    text="Sun (Origin)",
    xoffset=-30,
    yoffset=-30,
    color=color.black,
    height=12,
    box=True,
)

label(
    pos=r_Earth,
    text=f"Earth\n(0.3182, 0.9329, 0.0000) AU\nr_SE = {r_SE:.4f} AU",
    xoffset=30,
    yoffset=30,
    color=color.blue,
    height=12,
    box=True,
)

label(
    pos=r_Mars,
    text=f"Mars\n(1.3087, -0.4423, -0.0414) AU\nr_SM = {r_SM:.4f} AU",
    xoffset=30,
    yoffset=-30,
    color=color.red,
    height=12,
    box=True,
)

label(
    pos=r_Earth + r_EM_vec * 0.5,
    text=f"Earth-Mars Distance = {r_EM:.4f} AU\nAngle θ = {theta_deg:.1f}°\n(Not visible at midnight)",
    xoffset=-80,
    yoffset=40,
    color=color.black,
    height=13,
    box=True,
)

scene.waitfor("click")
