from vpython import arrow, color, cross, hat, mag, scene, vector

# 1. Define Vector A (3.0 * i - 4.0 * k)
A = vector(3.0, 0.0, -4.0)

# Calculate magnitude
A_mag = mag(A)

# --- Part (a): Parallel Unit Vector ---
# hat(v) returns the unit vector (v / mag(v))
u_parallel = hat(A)

# --- Part (b): Antiparallel Unit Vector ---
u_antiparallel = -hat(A)

# --- Part (c): Perpendicular Unit Vectors with no y-component ---
# Since A lies in the xz-plane, cross(A, vector(0, 1, 0)) gives a
# perpendicular direction in the xz-plane using the right-hand rule.
u_perp1 = hat(cross(A, vector(0, 1, 0)))
u_perp2 = -u_perp1

# --- Display Results ---
print(f"Vector A: {A}")
print(f"Magnitude of A: {A_mag}\n")
print(f"(a) Parallel unit vector:     {u_parallel}")
print(f"(b) Antiparallel unit vector: {u_antiparallel}")
print(f"(c) Perpendicular unit 1:     {u_perp1}")
print(f"    Perpendicular unit 2:     {u_perp2}")

# --- 3D Visualization Setup ---
scene.title = "3D Vector Visualization (Problem 1.55)"
scene.background = color.white

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

# Draw Vector A
arrow(pos=vector(0, 0, 0), axis=A, color=color.blue, shaftwidth=0.1)

# Draw Parallel Unit Vectors (Scaled slightly for visibility)
arrow(pos=vector(0, 0, 0), axis=u_parallel * 2, color=color.magenta, shaftwidth=0.08)
arrow(
    pos=vector(0, 0, 0), axis=u_antiparallel * 2, color=color.magenta, shaftwidth=0.08
)

# Draw Perpendicular Unit Vectors (Scaled slightly for visibility)
arrow(pos=vector(0, 0, 0), axis=u_perp1 * 2, color=color.green, shaftwidth=0.08)
arrow(pos=vector(0, 0, 0), axis=u_perp2 * 2, color=color.green, shaftwidth=0.08)

scene.waitfor("click")
