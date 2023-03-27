import numpy as np
import matplotlib.pyplot as plt
import csv


# Recieve the input of Voltage and time
time = []
voltage = []
with open('Ester.csv', 'r') as csvfile:
    print(csvfile)
    reader = csv.reader(csvfile)
    data = list(reader)

for i in data:
    time.append(float(i[0]))
    voltage.append(float(i[1]))

#plot voltage-time

plt.subplot(1,2,1)
plt.plot(time,voltage)
plt.xlabel('time')
plt.ylabel('voltage')
plt.show()
#Fourier transformation of voltage
Voltage = np.fft.fft(voltage)

#frequency axis for the Fourier
freq = np.fft.fftfreq(len(time), time[1] - time[0])

for i in Voltage:
    if abs(i)>1000:
        print(i)

"""       
#Plot the fourier transformation
#plt.subplot(1,2,2)
plt.plot(freq,Voltage)
plt.xlabel('time')
plt.ylabel('voltage')
#plt.xlim(5,100000)
plt.show()
"""