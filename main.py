from node import Node
import pygame
from itertools import combinations
C = 15000
K = 1
M = 1

pygame.init()
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill((255, 0, 0))

graph = [[1,2], [2,3], [1,3], [1,4]]
nodes_dict = dict()
nodes = []
for num1, num2 in graph:
	if num1 not in nodes:
		node1 = Node(num1)
		nodes_dict.update({num1: node1})
		nodes.append(node1)
	if num2 not in nodes_dict:
		node2 = Node(num2)
		nodes_dict.update({num2: node2})
		nodes.append(node2)
	node1 = nodes_dict[num1]
	node2 = nodes_dict[num2]
	node1.connected.append(node2)
	node2.connected.append(node1)

def draw():
	for node in nodes:
		pygame.draw.circle(screen, (200, 200, 200), (node.x, node.y), 5)
	for pair in combinations(nodes, 2):
		node1 = pair[0]
		node2 = pair[1]
		if node1 in node2.connected:
			pygame.draw.line(screen, (50, 100, 200), [node1.x, node1.y], [node2.x, node2.y], 1)



def apply_force(pair_array):  # физика
	for pair in pair_array:
		fst = pair[0]
		scnd = pair[1]
		dist = ((fst.x - scnd.x) ** 2 + (fst.y - scnd.y) ** 2) ** 0.5
		if (dist != 0):
			coulomb_force_x = (fst.x - scnd.x) * (C / (dist ** 2))
			coulomb_force_y = (fst.y - scnd.y) * (C / (dist ** 2))

			fst.accel[0] += coulomb_force_x
			fst.accel[1] += coulomb_force_y

			scnd.accel[0] -= coulomb_force_x
			scnd.accel[1] -= coulomb_force_y

			if (scnd in fst.connected):
				hooke_force_x = K * (fst.x - scnd.x)
				hooke_force_y = K * (fst.y - scnd.y)

				fst.accel[0] -= hooke_force_x
				fst.accel[1] -= hooke_force_y

				scnd.accel[0] += hooke_force_x
				scnd.accel[1] += hooke_force_y
pairs = [i for i in combinations(nodes, 2)]

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False


	#apply_force(pairs)
	screen.fill((255, 0, 0))
	#for node in nodes:
	#	node.move(0.01)
	draw()


pygame.quit()