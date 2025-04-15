# https://zhuanlan.zhihu.com/p/590190456 
# PyBullet仿真软件常用API函数 


import pybullet as p
import pybullet_data
import time 

##! 启用物理引擎 - 不同的线程
use_gui = True

if use_gui:
    physicsClient = p.connect(p.GUI)  # 返回一个物理服务器ID，如果连接不成功返回-1
else:
    physicsClient = p.connect(p.DIRECT)  # 在训练时采用这种方式连接

# 获取连接状态
print(p.getConnectionInfo(physicsClient))  # 返回一个列表 [isConnected, connectionMethod]
# 设置重力加速度
p.setGravity(0, 0, -9.8)  # X Y Z
# 添加资源路径：添加后，凡是在pybullet_data这个文件夹下的模型，都可以直接使用文件名加载，不需要再输入绝对路径。
p.setAdditionalSearchPath(pybullet_data.getDataPath())
# p.disconnect(physicsClient)  # 断开连接 关闭物理引擎服务器


#! 模拟器设置
# 逐步模拟
p.setRealTimeSimulation(1)  # 关闭实时模拟
p.setTimeStep(1./240.)  # 设置时间步
for i in range(10):
    p.stepSimulation()
    time.sleep(1 / 240) # Time in seconds. 仿真引擎暂停1/240秒，然后再进入下一个时间步，不影响仿真结果。


# # 实时模拟

# p.setRealTimeSimulation(1) # 实时仿真
# while True:
#     pass

# #! 重置仿真
# p.resetSimulation(physicsClientId) 

# #! 界面与显示设置 
