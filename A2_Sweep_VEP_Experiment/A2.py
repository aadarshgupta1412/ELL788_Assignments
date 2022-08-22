import matplotlib.pyplot as plt
import matplotlib.animation as anim
import matplotlib.colors as clr
import numpy as np

FREQUENCY = 10 # 10 Hz  
CPD_TIME = 10 # 30 seconds

def interval_finder(t):
    return int(t/(CPD_TIME * FREQUENCY))
    
def update(t):
    print(t)
    interval = interval_finder(t)

    a,b = 1,0
    if t % 2 == 0:
        a, b = 0,1

    x = a * np.ones((30, ncols))
    cpd = cpds[interval]
    # print('Starting CPD:', cpd)

    cycle_width = ncols//cpd
    layer_width = cycle_width//2

    for it in range(cpd):
        x[:, 2*it*layer_width : (2*it+1)*layer_width] = b

    mat.set_data(x)
    idx = t // 10
    label.set_text(f'{base} = {cpd}')
    
    return [mat]

cpds = [1,2,3,6,7,14,21]
ncols = 42 * 2

x = np.ones((30, ncols))

fig, ax = plt.subplots(1,1)
mat = ax.matshow(x, cmap='binary', vmin = 0, vmax=1)
base = 'Currently displaying CPD'
label = ax.text(ncols // 2, -15, "", ha='center', va='center', fontsize=20, color="Red")
ani = anim.FuncAnimation(fig, func=update, frames=iter(range(FREQUENCY * CPD_TIME * len(cpds))), repeat=False, interval=1000 / FREQUENCY)
ani.save('A2.mp4', writer='ffmpeg', fps=30)
