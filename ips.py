#como evitar libs.patiens
from libs.patient import Patient
from libs.cola import Cola

import random

# creacion de colas
queueNormal = Cola()
queuePriority = Cola()

## patiens by default
print("Runnig Creando pacientes")
p1 = Patient("Catalina", 12, "F")
p2 = Patient("Sofia", 22, "F")
p3 = Patient("Ana", 82, "F", True)
print("Registrando usuarios")


queueNormal.encolar(p1)
queueNormal.encolar(p2)
queuePriority.encolar(p3)


def printPatientInfo(aux):
	print(aux.name)
	print(aux.age)
	print(aux.gender)
	print(aux.priority)


##Dont change random
def inputPatient():

	#problemas con genrear
	random.seed(random.random())

	name = raw_input("Ingrese nombre : ") or "NN"
	age = int(raw_input("Ingrese edad : ") or random.randint(0,102))
 	genere = raw_input("Ingrese genero F / M  : ") or random.choice(["F", "M"])
	priority = int(raw_input("Ingrese Prioridad (Menor 1 a 10 Mayor ): ") or random.randint(1,10))
	p = Patient(name, age, genere, priority)
	queueNormal.encolar(p)


#hacer para que me mustre la Cola
def printPatientsInfo():
	while not queueNormal.es_vacia():
		p=queueNormal.desencolar()
		printPatientInfo(p)
		print("------------------------------")

new = 1
while (new):
	inputPatient()
	print("Se acaba de encolar un nuevo usuario")
	new = int(raw_input("Nuevo usuario (y)/n=0  : ") or 1)

printPatientsInfo()
