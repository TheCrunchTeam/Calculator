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
			"-   3- Salir                     -\n"
			"----------------------------------")
	return mensaje

def menuCalBasico():
	mensaje=("----------------------------------\n"
			"-  1-Sumar                       -\n"
			"-  2-Restar                      -\n"
			"-  3-Multiplicar                 -\n"
			"-  4-Divisíon                    -\n"
			"-  5-Salir Menú                  -\n"
			"----------------------------------")
	return mensaje	

def mensajeCalcucientifica():

	for i in range(3):
		os.system('cls')
		print("OO Xx    xX []")
		print("[]   x  x   []")
		print("[]    xx    []")
		print("[]   x  x   []")
		print("[] Xx    xX OO")
		time.sleep(0.9)
		os.system('cls')
		print("    ¡EN")
		print("CONSTRUCCIÓN...!")
		print("")
		time.sleep(0.9)
		os.system('cls')


print(mensajeOpcionesPri())

input()