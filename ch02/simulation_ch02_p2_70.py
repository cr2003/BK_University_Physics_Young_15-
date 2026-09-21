import numpy as np
from vpython import (
    box,
    color,
    cylinder,
    label,
    rate,
    scene,
    sphere,
    vector,
)

# --- 1. Scene Setup (Matching Figure P2.70 Perspective) ---
scene.title = "Figure P2.70: Egg Drop Simulation"
scene.width = 600
scene.height = 700
scene.background = color.white  # White background matching textbook style

# Camera view setup (Orthogonal front-facing view)
scene.center = vector(-1, 23, 0)
scene.forward = vector(0, 0, -1)  # Looking straight ahead
scene.range = 28  # Framing matching the textbook diagram

# --- 2. Physical Parameters ---
h_building = 46.0  # Building height (m)
h_prof = 1.80  # Professor height (m)
v_prof_x = 1.20  # Professor walking speed (m/s)
g = 9.80665  # Gravitational acceleration (m/s^2)

# Kinematic calculations
t_impact = np.sqrt(2 * (h_building - h_prof) / g)  # ~3.00 s
x_start_prof = v_prof_x * t_impact  # ~3.60 m

# --- 3. 3D World Objects ---

# Ground
ground = box(
    pos=vector(-2, -0.2, 0),
    size=vector(20, 0.4, 2),
    color=color.gray(0.5),
)

# Building (Aligned on the right, x = 0 is its left wall)
building_width = 8.0
building = box(
    pos=vector(building_width / 2, h_building / 2, 0),
    size=vector(building_width, h_building, 4),
    color=color.gray(0.75),
)

# Student on roof (Silhouetted figure on top-left edge of building)
student = sphere(
    pos=vector(0.3, h_building + 0.8, 0),
    radius=0.6,
    color=color.black,
)

# Professor (Walking from left to right toward x = 0)
prof_body = cylinder(
    pos=vector(-x_start_prof, 0, 0),
    axis=vector(0, h_prof - 0.3, 0),
    radius=0.25,
    color=color.red,
)
prof_head = sphere(
    pos=vector(-x_start_prof, h_prof - 0.15, 0),
    radius=0.22,
    color=color.red,
)

# Velocity arrow (Green arrow showing walking direction)
v_arrow = cylinder(
    pos=vector(-x_start_prof + 0.4, h_prof / 2, 0),
    axis=vector(1.2, 0, 0),
    radius=0.1,
    color=color.green,
)

# Egg
egg = sphere(
    pos=vector(0, h_building, 0),
    radius=0.25,
    color=color.orange,
    make_trail=True,
    trail_color=color.red,
    retain=50,
)

# Diagram Labels (Static annotations mimicking textbook figure)
label(
    pos=vector(-x_start_prof - 1.5, h_prof / 2, 0),
    text="1.80 m",
    box=False,
    color=color.black,
    height=12,
)
label(
    pos=vector(-x_start_prof, h_prof + 1.2, 0),
    text="v = 1.20 m/s",
    box=False,
    color=color.black,
    height=12,
)
label(
    pos=vector(building_width + 1.5, h_building / 2, 0),
    text="46.0 m",
    box=False,
    color=color.black,
    height=14,
)

# Dynamic status label
status_label = label(
    pos=vector(-4, h_building - 5, 0),
    text="Ready",
    box=False,
    color=color.blue,
    height=13,
)

# --- 4. Simulation Loop ---
dt = 0.01
t = 0.0

rate(1)  # Initial pause before releasing egg

while t <= t_impact:
    rate(100)

    # 1. Update egg free fall
    y_egg = h_building - 0.5 * g * (t**2)
    egg.pos = vector(0, max(y_egg, h_prof), 0)

    # 2. Update professor position
    x_prof = -x_start_prof + v_prof_x * t
    prof_body.pos = vector(x_prof, 0, 0)
    prof_head.pos = vector(x_prof, h_prof - 0.15, 0)
    v_arrow.pos = vector(x_prof + 0.4, h_prof / 2, 0)

    # 3. Update time display
    status_label.text = f"t = {t:.2f} s"
    t += dt

# Final impact state
status_label.text = f"DIRECT HIT at t = {t_impact:.2f} s!"
status_label.color = color.red
egg.color = color.yellow
################### The End ###################
print("\n\nAnimation complete.")
scene.waitfor("click")
