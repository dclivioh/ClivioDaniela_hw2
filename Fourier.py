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

#Se utiliza implementacion propia de la transformada de Fourier para una señal.

def fourier(señal):
    N=len(señal)
    amplitudes=[]
    for k in range(N):
        suma=0
        for i in range(N):
            suma += señal[i]*np.exp(-2j*np.pi*k*i/N)
        amplitudes.append(suma)
    return amplitudes

#Ahora aplicamos esta implementacion para calcular la transformada de fourier de cada señal.

n1=len(señal1)
n2=len(señal2)
a1=np.array(fourier(señal1))[: int(n1/2)]  #Tomamos la mitad de los valores pues la otra mitad es la misma grafica reflejada.
a2=np.array(fourier(señal2))[:int(n2/2)]

#Se realiza implementacion propia para obtener los valores de las frecuencias.
print("\n Implementacion propia para hallar frecuencias")
dt1=t1[1]-t1[0]
w1=(np.arange(n1)/(n1*dt1))[:int(n1/2)]
dt2=t2[1]-t2[0]
w2=(np.arange(n2)/(n2*dt2))[:int(n2/2)]

#Se grafican las tranformadas de Fourier de ambas señales en funcion de las frecuencias.

figura=plt.figure(figsize=(10,10))

ax=figura.add_subplot(211)
ax2=figura.add_subplot(212)
figura.suptitle("Transformadas de Fourier de las señales en funcion de las frecuencias")

ax.plot(w1,abs(a1),c="navy", label="Amplitudes vs Frecuencias")
ax.set_xlabel("Frecuencia")
ax.set_ylabel("Amplitud")
ax.legend()

ax2.plot(w2,abs(a2),c="limegreen", label="Amplitudes vs Frecuencias")
ax2.set_xlabel("Frecuencia")
ax2.set_ylabel("Amplitud")
ax2.legend()

figura.savefig("grafica_transformadas.png")
plt.close()

#Se grafican los espectrogramas para cada señal

figura=plt.figure(figsize=(10,10))

ax=figura.add_subplot(211)
ax2=figura.add_subplot(212)

ax.specgram(señal1, Fs=dt1/n1)
ax.set_title("Espectrograma de las señales contiguas")
ax.set_xlabel("Tiempo")
ax.set_ylabel("Frecuencias")

ax2.specgram(señal2,Fs=dt2/n2)
ax2.set_title("Espectrograma de las señales superpuestas")
ax2.set_xlabel("Tiempo")
ax2.set_ylabel("Frecuencias")

figura.savefig("grafica_espectrogramas.png")
plt.close()
