# from pybullet_env.BasicEnvironment import SoftRobotBasicEnvironment
from pybullet_env.BasicEnvironment import SoftRobotBasicEnvironment
from environment.BasicEnvironment import BasicEnvironment
import numpy as np
import time 


if __name__ == "__main__":
    
    env = BasicEnvironment()
    env.move_arm(target_pos=np.array([0.4, 0., 0.35]),
                 target_ori=[np.pi/2, np.pi/2, 0], duration = 2)
    env.wait(1)
    
    # env = SoftRobotBasicEnvironment(gui=True)
    # env.add_a_cube(pos=[0.5, 0.5, 0.1], size=[0.1, 0.1, 0.1])
    # env.move_robot_ori(action=np.array([0.1, 0.2, 0.3]))
    
    t = 0
    dt = 0.01
    while True:
        t += dt
        
 
        pos = np.array([
            0.3 + 0.05 * np.sin(0.1*np.pi*t),
            0.0 + 0.1 * np.sin(0.1*np.pi*t),
            0.5 + 0.03 * np.sin(0.1*np.pi*t)
        ])
        ori = np.array([
            1.5 * np.sin(0.2*np.pi*t),
            np.pi/2 - 0.2 * np.sin(0.02*np.pi*t),
            0.0 * np.sin(0.02*np.pi*t),
        ])
        
        env.move_arm(target_pos=pos, target_ori=ori)
        p0,o0 = env.get_ee_state()




        env.wait(0.2)
        
        
        
    