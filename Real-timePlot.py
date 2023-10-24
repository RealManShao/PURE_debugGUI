import numpy as np

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore

app = pg.mkQApp("Plotting Example")
#mw = QtWidgets.QMainWindow()
#mw.resize(800,800)

win = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
win.resize(1000,600)
win.setWindowTitle('pyqtgraph example: Plotting')

plot = win.addPlot(title="Updating plot")
curve = plot.plot(pen='y')
data = np.sin(np.linspace(-np.pi/2,7/2*np.pi,200))

ptr = 0
def update():
    global curve, data, ptr, plot
    c=ptr%100
    i=data[c:c+101]
    #print (i)
    curve.setData(i)
    if ptr == 0:
        plot.enableAutoRange('xy', False)  ## stop auto-scaling after the first data set is plotted
    ptr += 1
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(20) #refresh rate

win.nextRow()

if __name__ == '__main__':
    pg.exec()