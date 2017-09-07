import time

def sumar(*args):
	result = 0
	for valor in args:
		result += valor
	return result

def multiplicar(*args):
	result = 1
	for valor in args:
		result *= valor
	return result


print(sumar(5,5))

time.sleep(0.2)