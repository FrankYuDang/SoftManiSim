# 这个代码的目的是看到编码的内部，
# 但是发现 你不需要理解里面的 内部逻辑

import time
import pybullet as p 
import pybullet_data
import numpy as np 


urdf = "ur5-suction"
simulationStepTime = 0.01
vis = True
bullet = p
p.connect(p.GUI if vis else p.Direct)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setGravity(0, 0, -9.81)
p.setTimeStep(simulationStepTime)

p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.resetDebugVisualizerCamera(cameraDistance=0.8,
                             cameraYaw = -15,
                             cameraPitch = -25,
                             cameraTargetPosition=[0.2,0,0.3])
_bullet = p
plane_id = p.loadURDF('plane.urdf')

_urdf = urdf
_FK_offset = np.array([0.0,-0.00,-0.0]) 

## load_robot(urdf = f'environment/urdf/{_urdf}.urdf',print_joint_info=True)
urdf_file = f'environment/urdf/{_urdf}.urdf'
robot_id = p.load(urdf_file, p.getQuaternionFromEuler([0,0,0]), useFixedBase=True)

while True:
    p.stepSimulation()
    


