import time
import os

#Creacion de Los menus

def mensajePrincipal():
	mensaje=("--------------------------\n"
		     "-     Calculator V1.0    -\n"
		    "--------------------------")
	return mensaje

def mensajeOpcionesPri():
	mensaje=("----------------------------------\n"
			"-   1- Calculadora Básica        -\n"
			"-   2- Calculadora Científica    -\n"
			"----------------------------------")
	return mensaje

def menuCalBasico():
	mensaje=("----------------------------------\n"
			"-  1-Sumar                       -\n"
			"-  2-Restar                      -\n"
			"-  3-Multiplicar                 -\n"
			"-  4-Divisíon                    -\n"
			"-  5-Salir Menú                  -\n"
		)



print(mensajeOpcionesPri())	

input()