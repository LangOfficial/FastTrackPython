import random

class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack
        
    def attack_player(self, player):
        damage = random.randint(self.attack - 2, self.attack + 2)
        player.hp -= damage

        print(f"{self.name} attacks you for {damage} damage!")
