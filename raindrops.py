import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy.random as npRand


npRand.seed()

'''
User Parameters
'''
winSize = 6
numDrops = 30 # max # of raindrops to generate per frame
rAvg = 0.15 # max radius of raindrops
plt.style.use('dark_background')
fig = plt.figure(figsize=(winSize,winSize))
ax = plt.axes(xlim=(0,1),ylim=(0,1))
plt.axis('off')
'''
Initialization
'''

drops = np.zeros(numDrops,dtype=[('position',float,2),
                                 ('size',float,1),
                                 ('growth',float,1),
                                 ('color',float,4)])

drops['position'] = npRand.uniform(0,1,(numDrops,2))
drops['growth'] = npRand.uniform(50,150,numDrops)

plot = ax.scatter(drops['position'][:,0],drops['position'][:,1],
                  s=drops['size'],lw=0.3,ec=drops['color'],facecolors="None")

def animate(frame):
    current = frame % numDrops # index of oldest raindrop
    drops['color'][:,3]-= 1.0/len(drops)
    drops['color'][:,3]= np.clip(drops['color'][:,3],0,1)
    drops['size']+=drops['growth']

    drops['position'][current]=npRand.uniform(0,1,2)
    drops['size'][current]=npRand.random()+4
    drops['color'][current]=(1,1,1,1)
    drops['growth'][current]=npRand.uniform(50,150)

    plot.set_ec(drops['color'])
    plot.set_sizes(drops['size'])
    plot.set_offsets(drops['position'])


anim = FuncAnimation(fig,animate,interval=20,repeat = True)
anim.save('raindrops.gif',writer='imagemagick')
plt.show()
