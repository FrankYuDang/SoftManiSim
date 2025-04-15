import pybullet as p

# Initialize PyBullet
p.connect(p.DIRECT)

# Define two transformations
parent_position = [1, 0, 0]  # Parent frame position
parent_orientation = [0, 0, 0, 1]  # Parent frame orientation (quaternion)

child_position = [0, 1, 0]  # Child frame position relative to parent
child_orientation = [0, 0, 0, 1]  # Child frame orientation relative to parent

# Combine transformations
world_position, world_orientation = p.multiplyTransforms(
    parent_position, parent_orientation,
    child_position, child_orientation
)

print("World Position:", world_position)
print("World Orientation (quaternion):", world_orientation)