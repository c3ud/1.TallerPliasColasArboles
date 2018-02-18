#como evitar libs.patiens
from libs.Patient import Patient
from libs.cola import Cola




def printPatientInfo(aux):
	print(aux.name)
	print(aux.age)
	print(aux.gender)
	print(aux.priority)


print("Runnig Creando pacientes")
p1 = Patient("Catalina", 12, "F")
p2 = Patient("Sofia", 22, "F")
p3 = Patient("Ana", 82, "F", True)

print("Registrando usuarios")

queueNormal = Cola()
queuePriority = Cola()

queueNormal.encolar(p1)
queueNormal.encolar(p2)
queuePriority.encolar(p3)


#hacer para que me mustre la Cola
#printPatientInfo(queueNormal.desencolar)
printPatientInfo(p1)


print(p1.isDead())
