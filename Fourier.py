import numpy as np
import matplotlib.pylab as plt
import wget
from scipy.fftpack import *

#Se almacenan los datos de los archivos .dat y se les asignan sus variables respectivas

url1='https://raw.githubusercontent.com/dclivioh/hw2_data/master/signal.dat'
signal=wget.download(url1)
datossignal=np.genfromtxt("signal.dat")

url2='https://raw.githubusercontent.com/dclivioh/hw2_data/master/signalSuma.dat'
signalSuma=wget.download(url2)
datossignalSuma=np.genfromtxt("signalSuma.dat")

t1=datossignal[:,0]
señal1=datossignal[:,1]
t2=datossignalSuma[:,0]
señal2=datossignalSuma[:,1]

#Ahora graficamos estas dos señales en un subplot

figura=plt.figure(figsize=(10,10))

ax=figura.add_subplot(211)
ax2=figura.add_subplot(212)

ax.plot(t1,señal1,c="darkmagenta",label="Amplitud vs. Tiempo")
ax.set_title("Amplitudes de las señales contiguas en funcion del tiempo")
ax.set_xlabel("Tiempo")
ax.set_ylabel("Amplitud")
ax.legend()

ax2.plot(t2,señal2,c="darkorange", label="Amplitud vs tiempo")
ax2.set_title("Amplitudes de las señales superpuestas en funcion del tiempo")
ax2.set_xlabel("Tiempo")
ax2.set_ylabel("Amplitud")
ax2.legend()

figura.savefig("grafica_señales.png")
plt.close()
