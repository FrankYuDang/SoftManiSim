import numpy as np
import time
import pybullet as p 

from pybullet_env.BasicEnvironment import SoftRobotBasicEnvironment
from visualizer.visualizer import ODE 

from pathlib import Path
import csv
import os 

# --- Configuration for Saving Data ---
SAVE_DATA = True # Set to True to save data
OUTPUT_DIR = Path("./output_data/my_yomo") #! ./ means the workingspace directory
OUTPUT_DIR.mkdir(parents=True, exist_ok=True) 
TIMESTAMP = time.strftime("%Y%m%m_%H%M%S")
FILENAME = OUTPUT_DIR / f"yomo_run_{TIMESTAMP}.csv" # Construct hte full file path 

FIELDNAMES = ['time', 'cable1', 'cable2', 'cable3', 'head_x', 'head_y', 'head_z']
# --- End Configuration ---        

if __name__ == "__main__":
    
    yomo = SoftRobotBasicEnvironment(number_of_segment=1, head_color=[1,0.75, 1])
 
    t = 0
    dt = 0.01
    counter = 0
    # --- Initialize CSV file and writer ---
    csv_file = None
    csv_writer = None
    if SAVE_DATA: 
        csv_file = open(FILENAME, mode='a', newline='', encoding='utf-8')
        csv_writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)
        
        if csv_file.tell() == 0:
            csv_writer.writeheader()
    try:
        while True:
            t += dt
            counter += 1
            #TODO this part substitute the real data
            yomo_cable_1 = 0
            yomo_cable_2 = .005*np.sin(0.5*np.pi*t+2+5)
            yomo_cable_3 = .005*np.sin(0.5*np.pi*t+2+5)
            
            yomo.move_robot_ori(action=np.array([0.0, yomo_cable_1, yomo_cable_2]),
                                base_pos = np.array([0.0, 0.0, 1.0]), #修改底座
                                base_orin= np.array([0, 0, -np.pi/2])) #修改底座     
            
            head_pose, head_ori = yomo.calc_tip_pos(action=np.array([0.0, yomo_cable_1, yomo_cable_2]),
                                base_pos = np.array([0.0, 0.0, 1.0]), #修改底座
                                base_orin= np.array([0, 0, -np.pi/2])) #修改底座     

            # --- feature: Save the current data row ---
            if SAVE_DATA and csv_writer is not None:
                data_row = {
                    'time': t,
                    'cable1': yomo_cable_1,
                    'cable2': yomo_cable_2,
                    'cable3': yomo_cable_3,
                    'head_x': head_pose[0],
                    'head_y': head_pose[1],
                    'head_z': head_pose[2]
                }
                csv_writer.writerow(data_row)
            
            if counter % 200 == 0:
                print("hello world")
                formatted_head_pose = [f"{head_pose:.2f}" for head_pose in head_pose]
                formatted_head_ori = [f"{head_ori:.2f}" for head_ori in head_ori]
                print(f"the time at {t:.2f}, the head position is {formatted_head_pose}, and the orientation is {formatted_head_ori}")
                
    except KeyboardInterrupt:
        print("\n[info] Program interrupted by user.")
        
    finally:
        if csv_file is not None:
            csv_file.close()
            print(f"[info] Data saved to {FILENAME}.")

                    

                
        
            