import numpy as np
import matplotlib.pylab as plt

#Almacenamos los datos y les asignamos sus variables respectivas
datos=np.genfromtxt("resultados.dat")

t=datos[:,0]
u1=datos[:,1]
u2=datos[:,2]
u3=datos[:,3]
v1=datos[:,4]
v2=datos[:,5]
v3=datos[:,6]

#Se grafican las tres posiciones u en un subplot
figura=plt.figure(figsize=(10,10))
figura.suptitle("Posicion vs Tiempo")
ax=figura.add_subplot(311)
ax2=figura.add_subplot(312)
ax3=figura.add_subplot(313)

ax.plot(t,u1,c="crimson",label="Posicion u1 vs Tiempo")
ax.set_xlabel("Tiempo")
ax.set_ylabel("U1")
ax.legend()

ax2.plot(t,u2,c="royalblue", label="Posicion u2 vs Tiempo")
ax2.set_xlabel("Tiempo")
ax2.set_ylabel("U2")
ax2.legend()

ax3.plot(t,u3,c="seagreen", label="Posicion u3 vs Tiempo")
ax3.set_xlabel("Tiempo")
ax3.set_ylabel("U3")
ax3.legend()

figura.savefig("grafica_Ui.png")
plt.close()

#Se almacenan los datos y se le asignan sus variables correspondientes.
datosw=np.genfromtxt("resultados_frec.dat")

w=datosw[:,0]
umax1=datosw[:,1]
umax2=datosw[:,2]
umax3=datosw[:,3]

#Se grafican las amplitudes máximas en funcion de las frecuencias
figura2=plt.figure(figsize=(10,10))
figura2.suptitle("Amplitud maxima vs Frecuencia")
ax4=figura2.add_subplot(311)
ax5=figura2.add_subplot(312)
ax6=figura2.add_subplot(313)

ax4.plot(w,umax1,c="lightseagreen",label="Amplitud max u1 vs Frecuencia")
ax4.set_xlabel("Frecuencia")
ax4.set_ylabel("Umax1")
ax4.legend()

ax5.plot(w,umax2,c="slateblue", label="Amplitud max u2 vs Frecuencia")
ax5.set_xlabel("Frecuencia")
ax5.set_ylabel("Umax2")
ax5.legend()

ax6.plot(w,umax3,c="deeppink", label="Amplitud max u3 vs Frecuencia")
ax6.set_xlabel("Frecuencia")
ax6.set_ylabel("Umax3")
ax6.legend()

figura2.savefig("grafica_wAmax.png")
plt.close()
