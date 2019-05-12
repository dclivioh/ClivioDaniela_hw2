Resultados_hw2.pdf: Resultados_hw2.tex grafica_senal.pdf grafica_transformadas.pdf grafica_espectrograma.pdf grafica_senaltemblor.pdf grafica_transformadatemblor.pdf grafica_espectrogramatemblor.pdf grafica_ui.pdf grafica_wAmax.pdf
			pdflatex Resultados_hw2.tex

grafica_senal.pdf grafica_transformadas.pdf grafica_espectrograma.pdf grafica_senaltemblor.pdf grafica_transformadatemblor.pdf grafica_espectrogramatemblor.pdf: Fourier.py
		python3 Fourier.py

grafica_ui.pdf grafica_wAmax.pdf: Plots_hw2.py resultados_umax.dat resultadosw1.dat resultadosw2.dat resultadosw3.dat resultadosw4.dat
		python3 Plots_hw2.py

resultados_umax.dat resultadosw1.dat resultadosw2.dat resultadosw3.dat resultadosw4.dat: a.out
		./a.out

a.out: Edificio.cpp
		g++ Edificio.cpp
