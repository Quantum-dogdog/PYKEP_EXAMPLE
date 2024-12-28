import pykep as pk
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
'''
EARTH_R = 63781400
pk.util.load_spice_kernel("D:/bsp/de405.bsp")
earth = pk.planet.spice('EARTH', 'SUN', 'ECLIPJ2000', 'NONE', pk.MU_SUN, pk.MU_EARTH, EARTH_R, EARTH_R*1.05)
r,v = earth.eph(pk.epoch(9500))
print(r,v)
#print(pk.MU_EARTH)#398600441800000

apophis = pk.planet.mpcorb('99942   19.2   0.15 K107N 202.49545  126.41859  204.43202    3.33173  0.1911104  1.11267324   0.9223398  1 MPO164109  1397   2 2004-2008 0.40 M-v 3Eh MPCAPO     C802  (99942) Apophis            20080109')

H = apophis.H

print(H)

io = pk.planet.gtoc6('io')

print(io)
'''


pk.util.load_spice_kernel("D:/bsp/jup365.bsp")
europa = pk.planet.spice('EUROPA', 'JUPITER', 'ECLIPJ2000', 'NONE')


# 假设的epoch列表
epochs = list(range(9500, 9600))
# 使用列表推导式来获取每个epoch的欧罗巴位置和速度
ephemerides = [europa.eph(pk.epoch(e)) for e in epochs]

# 分别提取位置和速度
positions = [eph[0] for eph in ephemerides]
velocities = [eph[1] for eph in ephemerides]


ganymede = pk.planet.spice('GANYMEDE', 'JUPITER', 'ECLIPJ2000', 'NONE')



# 使用列表推导式来获取每个ganymede的欧罗巴位置和速度
ephemerides1 = [ganymede.eph(pk.epoch(e)) for e in epochs]

# 分别提取位置和速度
positions1 = [eph[0] for eph in ephemerides1]
velocities1 = [eph[1] for eph in ephemerides1]

# 创建3D图
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制木星（原点）
ax.scatter([0], [0], [0], color='yellow', s=100, label='Jupiter')

# 绘制每个epoch的欧罗巴位置
for pos in positions:
    ax.scatter(pos[0], pos[1], pos[2], color='red', s=10)
ax.scatter([], [], [], color='red', s=10, label='Europa')
# 绘制每个ganymede的欧罗巴位置
for pos in positions1:
    ax.scatter(pos[0], pos[1], pos[2], color='green', s=10)
ax.scatter([], [], [], color='green', s=10, label='Ganymede')

# 设置坐标轴标签和标题
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Plot of Europa\'s Positions Relative to Jupiter from Epoch 9500 to 9510')

# 添加图例
ax.legend()

# 显示图形
plt.show()
