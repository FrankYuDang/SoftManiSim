## 重要
#! 重要 明白了创建现实物体逻辑 

import pybullet as p 
import pybullet_data
import numpy as np

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.createCollisionShape(p.GEOM_PLANE)
p.createMultiBody(0,0)

sphereRadius = 0.05
colSphereId = p.createCollisionShape(p.GEOM_SPHERE, radius=sphereRadius)
colBoxId = p.createCollisionShape(p.GEOM_BOX,
                                  halfExtents=[sphereRadius, sphereRadius, sphereRadius])

# 两个变换
pos1 = [1, 0, 1]
orn1 = p.getQuaternionFromEuler([0, 0, np.pi/2]) # 90 degree around Z-axis

pos2 = [0, 1, 0]
orn2 = p.getQuaternionFromEuler([np.pi/2, 0, 0]) # 90 degress around X-axis
# 组合变换
pos_combined, orn_combined = p.multiplyTransforms(pos1, orn1,
                                                  pos2, orn2,)

orn_combined_euler = p.getEulerFromQuaternion(orn_combined)

print(f"orn1 :{orn1}")
print(f"orn2 :{orn2}")
print(f" Combined Position: {pos_combined}")
print(f"Combined Orientation: {orn_combined}")
print(f"Combined Orientation (Euler): {orn_combined_euler}")


visualShapeId = -1

sphereUid = p.createMultiBody(baseMass=0.0,
                              baseCollisionShapeIndex=colSphereId,
                              baseVisualShapeIndex=visualShapeId,
                              basePosition = pos1,
                              baseOrientation = orn1) 

sphereUid = p.createMultiBody(baseMass=0.0,
                              baseCollisionShapeIndex=colBoxId,
                              baseVisualShapeIndex=visualShapeId,
                              basePosition = pos_combined,
                              baseOrientation = orn_combined) 

while True:
    p.stepSimulation()



"""
self._relif(class) = __init__ 

"""