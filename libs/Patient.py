import random

class Patient:

	name = ""
	age =  0
	gender = ""
	priority = 0

	def __init__(self, name, age, gender, priority=1):
		self.name = name
		self.age = age
		self.gender = gender
		self.priority = priority


	def isDead(self):
		return random.choice(["Fallecio", "Vivo"])
