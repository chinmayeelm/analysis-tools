"""Written by Chinmayee.

Code to analyse Open-ephys recording data stored in Open-ephys file format
"""
import OpenEphys
from scipy import signal
import scipy
import pyqtgraph as pg
import matplotlib.pyplot as plt
from pyqtgraph.Qt import QtGui
import numpy as np
import matplotlib as mpl


rec = OpenEphys.loadContinuous(
    "/home/chetana/Documents/Work/OEdata/2017-11-01_CH/100_CH1.continuous")


order = 5
fs = 30000.0
nyq = 0.5 * fs
lowcut = 150.0/nyq
highcut = 1000.0/nyq

b, a = scipy.signal.butter(
    order, [lowcut, highcut], btype='bandpass', analog=False, output='ba')
filtered_data = scipy.signal.filtfilt(b, a, rec['data'])

a = float(rec['header']['sampleRate'])
print (rec['header']['sampleRate'])
print type(rec['timestamps'])
time = rec['timestamps']
print time
total_recording_time = float(len(filtered_data))/float(rec['header']['sampleRate'])
#total_recording_time_ = np.ceil(total_ recording_time)

t = np.linspace(time[0], time[-1], 5)
#t = str(t)
#print t

#plt.xlabel('time (seconds)')
# plt.grid(True)
# plt.axis('tight')
#plt.legend(loc='upper left')
# plt.show()
# axis.setLabel('left', "Y Axis", units='uV')
# axis.setLabel('bottom', "X Axis", units='time')

'''
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
'''

label_size = 15
mpl.rcParams['xtick.labelsize'] = label_size
mpl.rcParams['ytick.labelsize'] = label_size

plt.figure("Suction electrode recording from VNC(filtered)")
plt.plot(filtered_data)
# plt.title("Suction electrode recording from VNC(filtered)", fontsize=20)
#plt.plot(t*float(rec['header']['sampleRate']))
plt.ylabel('LFP (uV)', fontsize=20)
plt.xlabel('time', fontsize=20)
plt.xticks([])


plt.figure("Suction electrode recording from VNC(raw plot)")
plt.plot(rec['data'])
# plt.title("Suction electrode recording from VNC", fontsize=20)
plt.ylabel('LFP (uV)', fontsize=20)
plt.xlabel('time', fontsize=20)
plt.xticks([])


plt.show()
# QtGui.QApplication.instance().exec_()
