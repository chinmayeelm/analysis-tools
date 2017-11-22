"""Written by Chinmayee.

Code to analyse Open-ephys recording data stored in Open-ephys file format
"""
import OpenEphys
from scipy.signal import butter, lfilter
import pyqtgraph as pg
import matplotlib.pyplot as plt
from pyqtgraph.Qt import QtGui


""" Creates bandpass filter """


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='bandpass', analog=False)
    return b, a


""" Uses the above filter to give filtered data """


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


rec = OpenEphys.loadContinuous(
    "/home/chetana/Documents/Work/OEdata/2017-11-01_04-11-56/100_CH1.continuous")

fs = 30000.0
lowcut = 150.0
highcut = 1500.0

filtered_data = butter_bandpass_filter(
    rec['data'], lowcut, highcut, fs, order=6)

#plt.xlabel('time (seconds)')
#plt.hlines([-a, a], 0, T, linestyles='--')
# plt.grid(True)
# plt.axis('tight')
#plt.legend(loc='upper left')

# plt.show()

# axis.setLabel('left', "Y Axis", units='uV')
# axis.setLabel('bottom', "X Axis", units='time')


app = QtGui.QApplication([])
# win = pg.GraphicsWindow(title="Response to tactile stimulus on cephalic hair")
# win.resize(1000, 600)
# win.setWindowTitle('Suction electrode recording from VNC')
pg.setConfigOptions(antialias=True)
# p1 = win.addPlot(time, filtered_data, title="Suction electrode recording from VNC")
p1 = pg.plot(filtered_data,
             title="Suction electrode recording from VNC (filtered)")
p1.setLabel('left', "Y Axis", units='uV')
p1.setLabel('bottom', "X Axis", units='time')

p2 = pg.plot(
    rec['data'], title="Suction electrode recording from VNC (Raw data)")
p2.setLabel('left', "Y Axis", units='uV')
p2.setLabel('bottom', "X Axis", units='time')


QtGui.QApplication.instance().exec_()
