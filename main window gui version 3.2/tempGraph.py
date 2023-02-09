import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time


def newgraph():
    style.use("ggplot")

    fig = plt.figure(None,(100,100))
    ax1 = fig.add_subplot(1,1,1)

    def animate(i):
        pullData = open("openai.csv","r").read()
        dataArray = pullData.split('\n')
        xar = []
        yar = []
        for eachLine in dataArray:
            try:
                if len(eachLine)>1:
                    x,y = eachLine.split(',')
                    xar.append(int(x))
                    yar.append(int(y))
            except: pass
        ax1.clear()
        try: ax1.plot(xar[(len(xar)-50):],yar[len(yar)-50:])
        except:ax1.plot(xar,yar)
    ani = animation.FuncAnimation(fig, animate, interval=1000)
    plt.show()
    
newgraph()