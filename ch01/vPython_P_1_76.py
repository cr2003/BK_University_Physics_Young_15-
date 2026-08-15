from vpython import arrow, color, label, scene, sphere, vector

# --- Physical Values ---
q = -8.00e-6  # C
v_mag = 3.00e4  # m/s
B_mag = 5.00  # T

v_vec = vector(v_mag, 0, 0)
B_vec = vector(0, -B_mag, 0)

# F = q * (v x B)
v_cross_B = v_vec.cross(B_vec)
F_vec = q * v_cross_B  # 1.2 N in +z

# --- Visual Scaling ---
# Scale vectors for clear rendering in the 3D canvas
scale_v = 1.0 / 1.0e4  # Scale velocity
scale_B = 0.5  # Scale magnetic field
scale_F = 2.0  # Scale force

# --- 3D Scene Setup ---
scene.title = "3D Magnetic Force Visualization: F = q(v x B) (Problem 1.76)"
scene.background = color.white
scene.center = vector(1.5, -1.0, 1.0)
scene.range = 4.5

# Light Gray Reference Axes
axis_len = 3.5
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

# Particle (Negative Charge)
sphere(pos=vector(0, 0, 0), radius=0.2, color=color.cyan)

# Velocity Vector v (Blue)
arrow(
    pos=vector(0, 0, 0),
    axis=v_vec * scale_v,
    color=color.blue,
    shaftwidth=0.08,
)

# Magnetic Field Vector B (Green)
arrow(
    pos=vector(0, 0, 0),
    axis=B_vec * scale_B,
    color=color.green,
    shaftwidth=0.08,
)

# Force Vector F (Red)
arrow(
    pos=vector(0, 0, 0),
    axis=F_vec * scale_F,
    color=color.red,
    shaftwidth=0.08,
)

# --- Labels ---
label(
    pos=vector(0, 0, 0),
    text="q = -8.00 μC",
    xoffset=-40,
    yoffset=-30,
    color=color.black,
    height=12,
    box=True,
)

label(
    pos=v_vec * scale_v,
    text="Velocity v\n3.00 × 10⁴ m/s (+x)",
    xoffset=30,
    yoffset=20,
    color=color.blue,
    height=12,
    box=True,
)

label(
    pos=B_vec * scale_B,
    text="Magnetic Field B\n5.00 T (-y)",
    xoffset=30,
    yoffset=-30,
    color=color.green,
    height=12,
    box=True,
)

label(
    pos=F_vec * scale_F,
    text=f"Force F = {F_vec.mag:.2f} N (+z)",
    xoffset=30,
    yoffset=30,
    color=color.red,
    height=12,
    box=True,
)

scene.waitfor("click")
