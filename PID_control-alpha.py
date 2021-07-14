import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

fig = plt.figure()

kp = 1 # P制御
ki = 0 # I制御
kd = 0 # D制御

bx = 0; by = 0
bvx = bvy = 0
integral_x = integral_y = 0
errorx = errory = 0
dif_x = dif_y = 0

def update(t):
    global bx,by,bvx,bvy,integral_x,integral_y,errorx,errory,dif_x,dif_y
    plt.cla() # 現在描写されているグラフを消去
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    dt = 0.05
    t *= dt
    ax,ay = np.cos(t),np.sin(t)
    # 偏差
    dif_x = (ax - bx) - errorx
    dif_y = (ay - by) - errory
    errorx = (ax - bx) 
    errory = (ay - by) 
    integral_x += errorx
    integral_y += errory
    # PI制御
    bvx += errorx * kp + integral_x * ki + dif_x * kd
    bvy += errory * kp + integral_y * ki + dif_y * kd
    bx += bvx * dt 
    by += bvy * dt 
    plt.plot(ax,ay,'o')
    plt.plot(bx,by,'o')

ani = animation.FuncAnimation(fig, update, interval=30, frames=251)
# ani.save("P.gif", writer="imagemagick")
# plt.close()
plt.show()
