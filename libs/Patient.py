import random

class Patient:

	name = ""
	age =  0
	gender = ""
	priority = False

	def __init__(self, name, age, gender, priority=False):
		self.name = name
		self.age = age
		self.gender = gender
		self.priority = priority


	def isDead(self):
		return random.choice(["Dead", "Alive"])
