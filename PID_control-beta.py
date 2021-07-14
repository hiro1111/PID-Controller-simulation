import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

kp = 1 # P制御
ki = 1 # I制御
kd = 0 # D制御

bx = 0; by = 0
bvx = bvy = 0
errorx = [0]*3 # [0]は現在の偏差 [1]はひとつ前 [2]はふたつ前
errory = [0]*3

def update(t):
    global bx,by,bvx,bvy,errorx,errory
    plt.cla() # 現在描写されているグラフを消去
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    dt = 0.05
    t *= dt
    ax,ay = np.cos(t),np.sin(t)
    # 偏差
    errorx[0] = (ax - bx) 
    errory[0] = (ay - by) 
    # PID制御
    bvx += kp * (errorx[0]-errorx[1]) + ki * errorx[0] + kd * (errorx[0] - 2*errorx[1] + errorx[2])
    bvy += kp * (errory[0]-errory[1]) + ki * errory[0] + kd * (errory[0] - 2*errory[1] + errory[2])
    bx += bvx * dt 
    by += bvy * dt 
    plt.plot(ax,ay,'o')
    plt.plot(bx,by,'o')
    for i in (1,0):
        errorx[i+1] = errorx[i]
        errory[i+1] = errory[i]

ani = animation.FuncAnimation(fig, update, interval=30, frames=251)
# ani.save("P.gif", writer="imagemagick")
# plt.close()
plt.show()