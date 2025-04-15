#the visual and collision doesn;t have to be the same, but it is more efficient to use the same mesh for both
import pybullet as p
import pybullet_data

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# 创建一个立方体碰撞形状
collision_shape = p.createCollisionShape(p.GEOM_BOX, halfExtents=[0.1, 0.1, 0.1])
visual_shape_box = p.createVisualShape(p.GEOM_BOX, halfExtents=[0.1, 0.1, 0.1], rgbaColor=[0, 1, 0, 1])

# 创建一个球体视觉形状
visual_shape_sphere = p.createVisualShape(p.GEOM_SPHERE, radius=0.2, rgbaColor=[1, 0, 0, 1])

# 创建多体，使用不同的碰撞和视觉形状
body_id = p.createMultiBody(baseMass=1,
                            baseCollisionShapeIndex=collision_shape,
                            baseVisualShapeIndex=visual_shape_box,
                            basePosition=[0, 0, 1])

while True:
    p.stepSimulation()