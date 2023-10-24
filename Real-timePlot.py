import numpy as np

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore

app = pg.mkQApp("Plotting Example")
#mw = QtWidgets.QMainWindow()
#mw.resize(800,800)

win = pg.GraphicsLayoutWidget(show=True, title="plotting examples")
win.resize(1000,600)
win.setWindowTitle('Plotting')

plot1 = win.addPlot(title="Updating plot")
plot1.setYRange(-2,2)
curve = plot1.plot(pen='y')
data = np.sin(np.linspace(-1/2*np.pi,3/2*np.pi,100))

ptr = 0
i=[0]*100 #create a empty list to hold the plot data
def update():
    global curve, data, ptr, plot1,i
    c=ptr%100
    i.pop(0)
    i.append(data[c])
    curve.setData(i)
    # if ptr == 0:
    #     plot.enableAutoRange('xy', False)  ## stop auto-scaling after the first data set is plotted
    ptr += 1
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(20) #refresh rate

win.nextRow()

if __name__ == '__main__':
    pg.exec()