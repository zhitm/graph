from random import randint
class Node:
	def __init__(self, number):
		self.number = number
		self.connected = []
		self.accel = [0, 0]
		self.speed = [0, 0]
		self.x = randint(400, 600)
		self.y = randint(400, 600)

	def move(self, dt):
		self.speed[0] += dt * self.accel[0]
		self.speed[1] += dt * self.accel[1]
		self.x += int(dt*self.speed[0])
		self.y += int(dt*self.speed[1])


