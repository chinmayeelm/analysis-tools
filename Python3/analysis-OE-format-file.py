import OpenEphys
from scipy.signal import butter, lfilter
import pyqtgraph as pg
import matplotlib.pyplot as plt


def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='bandpass', analog=False)
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y


rec = OpenEphys.loadContinuous(
    "~/Documents/Work/OEdata/2017-11-01_04-11-56/100_CH1.continuous")

fs = 30000.0
lowcut = 150.0
highcut = 1500.0

y = butter_bandpass_filter(rec['data'], lowcut, highcut, fs, order=6)
pg.plot(y, title='Filtered signal')
#plt.xlabel('time (seconds)')
#plt.hlines([-a, a], 0, T, linestyles='--')
# plt.grid(True)
# plt.axis('tight')
#plt.legend(loc='upper left')

# plt.show()

pg.plot(rec['data'], title='raw data')
#axis.setLabel('left', "Y Axis", units='uV')
#axis.setLabel('bottom', "X Axis", units='time')

pg.QtGui.QApplication.exec_()
