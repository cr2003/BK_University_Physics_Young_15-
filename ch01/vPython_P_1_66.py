from vpython import arrow, color, label, scene, vector

# 1. Define vector legs
l_1 = vector(-14.0, 0, 0)  # West
l_2 = vector(0, 0, 22.0)  # Upward
l_3 = vector(0, 12.0, 0)  # North
l_4 = vector(6.0, 0, 0)  # East

# Accumulated positions (Tip-to-Tail connections)
pos_0 = vector(0, 0, 0)
pos_1 = pos_0 + l_1
pos_2 = pos_1 + l_2
pos_3 = pos_2 + l_3
pos_4 = pos_3 + l_4  # Final balcony position

# Resultant movement from origin to final position
R = pos_4

# Calculate magnitude
print(f"Distance to friend: {R.mag:.1f} m")

# --- 3D Visualization Setup ---
scene.title = "3D Vector Visualization (Problem 1.66)"
scene.background = color.white

# --- Adjust Camera View (Shifts Origin Downward) ---
# Setting scene.center moves the camera target point.
# Shifting target point UP/LEFT causes the rendered objects to move DOWN/RIGHT.
scene.center = vector(-4.0, 6.0, 11.0)

# Draw Coordinate Axes
axis_length = 5
arrow(
    pos=vector(0, 0, 0),
    axis=vector(axis_length, 0, 0),
    color=color.gray(0.7),
    shaftwidth=0.05,
)  # X-axis
arrow(
    pos=vector(0, 0, 0),
    axis=vector(0, axis_length, 0),
    color=color.gray(0.7),
    shaftwidth=0.05,
)  # Y-axis
arrow(
    pos=vector(0, 0, 0),
    axis=vector(0, 0, axis_length),
    color=color.gray(0.7),
    shaftwidth=0.05,
)  # Z-axis

# --- Draw Vector legs connected Tip-to-Tail ---
arrow(pos=pos_0, axis=l_1, color=color.blue, shaftwidth=0.2)
arrow(pos=pos_1, axis=l_2, color=color.cyan, shaftwidth=0.2)
arrow(pos=pos_2, axis=l_3, color=color.green, shaftwidth=0.2)
arrow(pos=pos_3, axis=l_4, color=color.magenta, shaftwidth=0.2)

# Resultant Vector R (From origin to final position)
arrow(pos=pos_0, axis=R, color=color.red, shaftwidth=0.2)

# --- Add 3D Labels ---
# Key positions
label(
    pos=pos_0,
    text="Friend position (Origin)",
    xoffset=20,
    yoffset=-20,
    color=color.black,
    height=12,
    box=True,
)
label(
    pos=pos_4,
    text=f"Balcony (You)\nDistance: {R.mag:.1f} m",
    xoffset=20,
    yoffset=20,
    color=color.red,
    height=12,
    box=True,
)

# Vector displacement step labels (positioned at the midpoint of each vector)
label(
    pos=pos_0 + l_1 / 2,
    text="1. West (14 m)",
    xoffset=20,
    yoffset=20,
    color=color.blue,
    height=10,
    box=False,
    opacity=0,
)
label(
    pos=pos_1 + l_2 / 2,
    text="2. Upward (22 m)",
    color=color.cyan,
    height=10,
    box=False,
    opacity=0,
)
label(
    pos=pos_2 + l_3 / 2,
    text="3. North (12 m)",
    color=color.green,
    height=10,
    box=False,
    opacity=0,
)
label(
    pos=pos_3 + l_4 / 2,
    text="4. East (6 m)",
    color=color.magenta,
    xoffset=-20,
    yoffset=-20,
    height=10,
    box=False,
    opacity=0,
)

scene.waitfor("click")
