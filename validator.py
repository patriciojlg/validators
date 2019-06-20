

"""
VALIDADOR DE RUTs
"""
from itertools import cycle

#Recibe un rut con cualquier fomato ej. 5.333.443-8 o 5333443-8
def validarRut(rut):
	rut = rut.upper();
	rut = rut.replace("-","")
	rut = rut.replace(".","")
	aux = rut[:-1]
	dv = rut[-1:]
 
 #Realiza la formula de sumar hacia adelante y hacia atrás los numeros del rut 
	revertido = map(int, reversed(str(aux)))
	factors = cycle(range(2,8))
	s = sum(d * f for d, f in zip(revertido,factors))
	res = (-s)%11
 
 #compara el resultado de lo anterior con el codigo verificador, si son iguales o K = 10, arroja True sino False
	if str(res) == dv:
		return True
	elif dv=="K" and res==10:
		return True
	else:
		return False
