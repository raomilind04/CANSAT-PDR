import pyqtgraph as pg
import numpy as np

class graph_gyro:
    
    def __init__(self, widget):
        self.widget = widget
        self.widget.getPlotItem().setTitle("Gyro")

        self.widget.hideAxis('bottom')
        # adding legend
        self.widget.addLegend()
        self.pitch_plot = self.widget.plot(pen= pg.mkPen((255, 0, 0), width=3), name="Pitch")
        self.roll_plot = self.widget.plot(pen= pg.mkPen((0, 255, 0), width=3), name="Roll")
        self.yaw_plot = self.widget.plot(pen= pg.mkPen((0, 0, 255), width=3), name="Yaw")

        self.pitch_data = np.linspace(0, 0)
        self.roll_data = np.linspace(0, 0)
        self.yaw_data = np.linspace(0, 0)
        self.ptr = 0


    def update(self, pitch, roll, yaw):

        self.pitch_data[:-1] = self.pitch_data[1:]
        self.roll_data[:-1] = self.roll_data[1:]
        self.yaw_data[:-1] = self.yaw_data[1:]

        self.pitch_data[-1] = float(pitch)
        self.roll_data[-1] = float(roll)
        self.yaw_data[-1] = float(yaw)

        self.ptr += 1

        self.pitch_plot.setData(self.pitch_data)
        self.roll_plot.setData(self.roll_data)
        self.yaw_plot.setData(self.yaw_data)

        self.pitch_plot.setPos(self.ptr, 0)
        self.roll_plot.setPos(self.ptr, 0)
        self.yaw_plot.setPos(self.ptr, 0)