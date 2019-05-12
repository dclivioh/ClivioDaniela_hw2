import numpy as np
import matplotlib.pylab as plt

#Almacenamos los datos y les asignamos sus variables respectivas
datosu1=np.genfromtxt("resultadosw1.dat")
t1=datosu1[:,0]
u1=datosu1[:,1]

datosu2=np.genfromtxt("resultadosw2.dat")
t2=datosu2[:,0]
u2=datosu2[:,1]

datosu3=np.genfromtxt("resultadosw3.dat")
t3=datosu3[:,0]
u3=datosu3[:,1]

datosu4=np.genfromtxt("resultadosw4.dat")
t4=datosu4[:,0]
u4=datosu4[:,1]

#Se grafican las tres posiciones u en un subplot
figura=plt.figure(figsize=(10,10))
figura.suptitle("Comportamiento de cada piso del edificio durante el sismo a traves del tiempo.")
ax=figura.add_subplot(411)
ax2=figura.add_subplot(412)
ax3=figura.add_subplot(413)
ax4=figura.add_subplot(414)

ax.plot(t1,u1,c="mediumblue",label="Posicion u1 vs Tiempo para w1=0.6")
ax.set_xlabel("t")
ax.set_ylabel("u1(t)")
ax.legend()

ax2.plot(t2,u2,c="darkorange", label="Posicion u2 vs Tiempo para w2=1.8")
ax2.set_xlabel("t")
ax2.set_ylabel("u2(t)")
ax2.legend()

ax3.plot(t3,u3,c="mediumturquoise", label="Posicion u3 vs Tiempo para w3=2.6")
ax3.set_xlabel("t")
ax3.set_ylabel("u3(t)")
ax3.legend()

ax4.plot(t4,u4,c="blueviolet", label="Posicion u4 vs Tiempo para w4=4.0")
ax4.set_xlabel("t")
ax4.set_ylabel("u4(t)")
ax4.legend()

figura.savefig("grafica_ui.pdf")
plt.close()

#Se almacenan los datos y se le asignan sus variables correspondientes.
datosumax=np.genfromtxt("resultados_umax.dat")

w=datosumax[:,0]
umax1=datosumax[:,1]
umax2=datosumax[:,2]
umax3=datosumax[:,3]

#Se grafican las amplitudes máximas en funcion de las frecuencias
figura2=plt.figure(figsize=(10,10))
figura2.suptitle("Amplitudes máximas en función de las frecuencias dadas en cada piso del edificio (Piso 1, 2, 3 respectivamente)")
ax4=figura2.add_subplot(311)
ax5=figura2.add_subplot(312)
ax6=figura2.add_subplot(313)

ax4.plot(w,umax1,c="lightseagreen",label="Amplitud max u1 vs Frecuencia")
ax4.set_xlabel("Frecuencia")
ax4.set_ylabel("u1(t)max")
ax4.legend()

ax5.plot(w,umax2,c="slateblue", label="Amplitud max u2 vs Frecuencia")
ax5.set_xlabel("Frecuencia")
ax5.set_ylabel("u2(t)max")
ax5.legend()

ax6.plot(w,umax3,c="deeppink", label="Amplitud max u3 vs Frecuencia")
ax6.set_xlabel("Frecuencia")
ax6.set_ylabel("u3(t)max")
ax6.legend()

figura2.savefig("grafica_wAmax.pdf")
plt.close()
