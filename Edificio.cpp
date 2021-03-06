#include <iostream>
#include <math.h>
#include <fstream>

using namespace std;

//Implementamos código de Runge Kutta para calcular los valores de las posiciones u y velocidades v.
void RungeKutta(double dt,double *t,double (*F)(double ,double),double gamma, double k, double w, double m, int ncols, int n, double *u, double *v, double *k1, double *k2, double *k3, double *k4){
  for (int i=0;i<n;i++){
    t[i]=t[i-1]+dt;
    k1[0]=(v[(i-1)*ncols+0])*dt;
    k1[1]=(v[(i-1)*ncols+1])*dt;
    k1[2]=(v[(i-1)*ncols+2])*dt;
    k1[3]=dt/m*(-gamma*v[(i-1)*ncols+0]-2.0*k*u[(i-1)*ncols+0]+k*u[(i-1)*ncols+1] + F(t[i-1],w));
    k1[4]=dt/m*(-gamma*v[(i-1)*ncols+1]+k*u[(i-1)*ncols+0]-2.0*k*u[(i-1)*ncols+1]+k*u[(i-1)*ncols+2]);
    k1[5]=dt/m*(-gamma*v[(i-1)*ncols+2]+k*u[(i-1)*ncols+1]-k*u[(i-1)*ncols+2]);

    k2[0]=(v[(i-1)*ncols+0]+dt/2.0*k1[0])*dt;
    k2[1]=(v[(i-1)*ncols+1]+dt/2.0*k1[1])*dt;
    k2[2]=(v[(i-1)*ncols+2]+dt/2.0*k1[2])*dt;
    k2[3]=dt/m*(-gamma*(v[(i-1)*ncols+0]+dt/2.0*k1[3])-2.0*k*(u[(i-1)*ncols+0]+dt/2.0*k1[0])+k*(u[(i-1)*ncols+1]+dt/2.0*k1[1])+F(t[i-1]+dt/2,w));
    k2[4]=dt/m*(-gamma*(v[(i-1)*ncols+1]+dt/2.0*k1[4])+k*(u[(i-1)*ncols+0]+dt/2.0*k1[0])-2.0*k*(u[(i-1)*ncols+1]+dt/2.0*k1[1])+k*(u[(i-1)*ncols+2]+dt/2.0*k1[2]));
    k2[5]=dt/m*(-gamma*(v[(i-1)*ncols+2]+dt/2.0*k1[5])+k*(u[(i-1)*ncols+1]+dt/2.0*k1[1])-k*(u[(i-1)*ncols+2]+dt/2.0*k1[2]));

    k3[0]=(v[(i-1)*ncols+0]+dt/2.0*k2[0])*dt;
    k3[1]=(v[(i-1)*ncols+1]+dt/2.0*k2[1])*dt;
    k3[2]=(v[(i-1)*ncols+2]+dt/2.0*k2[2])*dt;
    k3[3]=dt/m*(-gamma*(v[(i-1)*ncols+0]+dt/2.0*k2[3])-2.0*k*(u[(i-1)*ncols+0]+dt/2.0*k2[0])+k*(u[(i-1)*ncols+1]+dt/2.0*k2[1])+F(t[i-1]+dt/2,w));
    k3[4]=dt/m*(-gamma*(v[(i-1)*ncols+1]+dt/2.0*k2[4])+k*(u[(i-1)*ncols+0]+dt/2.0*k2[0])-2.0*k*(u[(i-1)*ncols+1]+dt/2.0*k2[1])+k*(u[(i-1)*ncols+2]+dt/2.0*k2[2]));
    k3[5]=dt/m*(-gamma*(v[(i-1)*ncols+2]+dt/2.0*k2[5])+k*(u[(i-1)*ncols+1]+dt/2.0*k2[1])-k*(u[(i-1)*ncols+2]+dt/2.0*k2[2]));

    k4[0]=(v[(i-1)*ncols+0]+dt*k3[0])*dt;
    k4[1]=(v[(i-1)*ncols+1]+dt*k3[1])*dt;
    k4[2]=(v[(i-1)*ncols+2]+dt*k3[2])*dt;
    k4[3]=dt/m*(-gamma*(v[(i-1)*ncols+0]+dt*k3[3])-2.0*k*(u[(i-1)*ncols+0]+dt*k3[0])+k*(u[(i-1)*ncols+1]+dt*k3[1])+F(t[i-1]+dt,w));
    k4[4]=dt/m*(-gamma*(v[(i-1)*ncols+1]+dt*k3[4])+k*(u[(i-1)*ncols+0]+dt*k3[0])-2.0*k*(u[(i-1)*ncols+1]+dt*k3[1])+k*(u[(i-1)*ncols+2]+dt*k3[2]));
    k4[5]=dt/m*(-gamma*(v[(i-1)*ncols+2]+dt*k3[5])+k*(u[(i-1)*ncols+1]+dt*k3[1])-k*(u[(i-1)*ncols+2]+dt*k3[2]));
    for(int j=0;j<3;j++){
      u[i*ncols+j]=u[(i-1)*ncols+j]+1/6.0*(k1[j]+2.0*k2[j]+2.0*k3[j]+k4[j]);
      v[i*ncols+j]=v[(i-1)*ncols+j]+1/6.0*(k1[j+3]+2.0*k2[j+3]+2.0*k3[j+3]+k4[j+3]);
       }
    }
}

//Definimos la funcion del forzamiento externo a la estructura
double F(double t,double w){
  return sin(w*t);
}

int main(){
  // Implementamos las condiciones iniciales del problema
  double tf=30;
  double dt=0.01;
  int n=int(tf/dt);
  int ncols=3;
  double m=1000.0;
  double gamma=0.0;
  double k=2000;
  double w=1.0*sqrt(k/m);
  double *u;
  u=new double [n*ncols];
  double *v;
  v=new double [n*ncols];
  double *k1;
  k1=new double[6];
  double *k2;
  k2=new double[6];
  double *k3;
  k3=new double[6];
  double *k4;
  k4=new double[6];
  double *t;
  t= new double [n];
  double wf[100];
  double umax[100][3];
  double w1=0.6;
  double w2=1.8;
  double w3=2.6;
  double w4=4.0;
// Se inicializan los valores de u, v y tiempo t.
  for (int j;j<3;j++){
    int i=0;
    u[i*ncols+j]=0;
    v[i*ncols+j]=0;
    t[i]=0;
  }

//Llamamos a la función Runge Kutta.
  RungeKutta(dt,t,F,gamma,k,w1,m,ncols,n,u,v,k1,k2,k3,k4);

//Almacenamos los datos obtenidos en un archivo .dat
  ofstream archivo1;
  archivo1.open("resultadosw1.dat");
  for (int i = 0; i < n; i++) {
    archivo1 << t[i] << " " << u[i*ncols+0] << " " << u[i*ncols+1]<< " " << u[i*ncols+2]<< endl;
  }
  archivo1.close();

  //Llamamos a la función Runge Kutta.
    RungeKutta(dt,t,F,gamma,k,w2,m,ncols,n,u,v,k1,k2,k3,k4);

  //Almacenamos los datos obtenidos en un archivo .dat
    ofstream archivo2;
    archivo2.open("resultadosw2.dat");
    for (int i = 0; i < n; i++) {
      archivo2 << t[i] << " " << u[i*ncols+0] << " " << u[i*ncols+1]<< " " << u[i*ncols+2]<< endl;
    }
    archivo2.close();


    //Llamamos a la función Runge Kutta.
      RungeKutta(dt,t,F,gamma,k,w3,m,ncols,n,u,v,k1,k2,k3,k4);

    //Almacenamos los datos obtenidos en un archivo .dat
      ofstream archivo3;
      archivo3.open("resultadosw3.dat");
      for (int i = 0; i < n; i++) {
        archivo3 << t[i] << " " << u[i*ncols+0] << " " << u[i*ncols+1]<< " " << u[i*ncols+2]<< endl;
      }
      archivo3.close();


      //Llamamos a la función Runge Kutta.
        RungeKutta(dt,t,F,gamma,k,w4,m,ncols,n,u,v,k1,k2,k3,k4);

      //Almacenamos los datos obtenidos en un archivo .dat
        ofstream archivo4;
        archivo4.open("resultadosw4.dat");
        for (int i = 0; i < n; i++) {
          archivo4 << t[i] << " " << u[i*ncols+0] << " " << u[i*ncols+1]<< " " << u[i*ncols+2]<< endl;
        }
        archivo4.close();


//Se definen las condiciones iniciales de las amplitudes máximas para cada posicion en el tiempo.
  wf[0]=0.2*sqrt(k/m);
  RungeKutta(dt,t,F,gamma,k,wf[0],m,ncols,n,u,v,k1,k2,k3,k4);
  umax[0][0]=0;
  umax[0][1]=0;
  umax[0][2]=0;
  for(int j=0;j<3;j++){
    for(int i=0;i<n;i++){
    if(umax[0][j]<u[i*ncols+j]){
      umax[0][j]=u[i*ncols+j];
    }
    }
  }
  //Calculamos RungeKutta para diferentes valores de wf. Hallamos los valores máximos de amplitud para cada posición.
  for(int l=1;l<100;l++){
      double dw=(2.8*sqrt(k/m))/100;
      wf[l]=wf[l-1]+dw;
      RungeKutta(dt,t,F,gamma,k,wf[l],m,ncols,n,u,v,k1,k2,k3,k4);
      umax[l][0]=0;
      umax[l][1]=0;
      umax[l][2]=0;
      for(int j=0;j<3;j++){
        for(int i=0;i<n;i++){
        if(umax[l][j]<u[i*ncols+j]){
          umax[l][j]=u[i*ncols+j];
        }
        }
    }
  }
  //Almacenamos los datos en un archivo .dat
  ofstream archivo5;
  archivo5.open("resultados_umax.dat");
  for (int i = 0; i < 100; i++) {
    archivo5 << wf[i] << " " << umax[i][0] << " " << umax[i][1]<< " " << umax[i][2]<< endl;
  }
  archivo5.close();


    delete[] t;
    delete[] u;
    delete[] v;
}
