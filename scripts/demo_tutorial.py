# 03-27
# try pybullet load robot and create environment 

import pybullet as p 
import pybullet_data

# if __name__ == "__main__": 

p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# 加载urdf文件
robot_id = p.loadURDF("r2d2.urdf", [0, 0, 0])

#仿真环境初始化
p.setGravity(0, 0, -9.8)
p.setTimeStep(1./240.)

#创建刚体
plane_id = p.createCollisionShape(p.GEOM_PLANE)
p.createMultiBody(0, plane_id)

# 关节控制
for joint_index in range(p.getNumJoints(robot_id)):
    p.setJointMotorControl2(robot_id, 
                            joint_index,
                            p.VELOCITY_CONTROL,
                            targetVelocity=0)


while True:
    p.stepSimulation()
    
    
    
                            

