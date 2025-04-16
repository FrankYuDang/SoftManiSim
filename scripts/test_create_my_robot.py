import numpy as np
import time

from pybullet_env.BasicEnvironment import SoftRobotBasicEnvironment

if __name__ == "__main__":
    
    yomo = SoftRobotBasicEnvironment(bullet=bullet)
    
    t = 0
    dt = 0.01
    
    while True:
        t += dt
        
        yomo.move_robot_ori(action=np.array([0.0, yomo_cable_1, yomo_cable_2]),
                            base_pos = new_pose,
                            base_orin= base_orin)
        
        
        
        