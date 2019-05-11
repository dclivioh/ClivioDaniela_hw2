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
