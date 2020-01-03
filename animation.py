from matplotlib import pyplot as plt
from matplotlib import animation

from wave_class import Wave
            
wave=Wave()

fig = plt.figure()
ax = plt.axes(xlim=(-0.1, 1.1), ylim=(-1, 1))
line, = ax.plot([], [],lw=2)

def init():
    line.set_data([], [])
    return line,

#Create new wave at click location
def onClick(event):
    wave.new_wave(event.xdata)


def animate(i):
    global wave    
    wave.step()
    data=wave.get_wave()
    line.set_data(data[0],data[1])
    return line,


fig.canvas.mpl_connect('button_press_event', onClick)

anim = animation.FuncAnimation(fig, animate, frames=300,interval=5,
                               init_func=init, blit=True)