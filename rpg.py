class Character:
	def __init__(self, name, health_point, mana_point, attack, defense, level, experiences):
		self.name		  = name
		self.health_point = health_point
		self.attack		  = attack

	def __str__(self):
		return self.name

	def attacking(self, Character):
		print(self.name, 'attack', Character.name, 'with', self.attack)
		Character.health_point = Character.health_point - self.attack
		if Character.health_point < 0:
			print(Character.name, 'dead !')
		else:
			print(Character.name, 'got', Character.health_point, 'left')
		print()


if __name__ == '__main__':
	knight = Character('knight', health_point = 100, mana_point = 20, \
		attack = 30, defense = 10, level = 1, experiences = 0)

	for i in range(5):
		poring = Character('poring', health_point =  50, mana_point =  5, \
			attack =  5, defense = 15, level = 1, experiences = 0)

		while knight.health_point > 0 and poring.health_point > 0:
			if knight.health_point > 0:
				knight.attacking(poring)
			if poring.health_point > 0:
				poring.attacking(knight)

	file = open('rpg.txt', 'wb')

	file.write(bytes(knight.attack))

	file.close()

	file = open('rpg.txt', 'w')

	print(file.readline())
