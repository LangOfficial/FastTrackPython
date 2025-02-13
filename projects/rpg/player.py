import random
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.full_hp = 100
        self.attack = 10
        self.level = 1
        self.xp = 0
    
    def attack_enemy(self, enemy):
        damage = random.randint(self.attack - 2, self.attack + 2)
        enemy.hp -= damage
        print(f"You attack {enemy.name} for {damage} damage!")
    
    def level_up(self):
        self.level += 1
        self.full_hp += 20
        self.attack += 5
        self.xp = 0
        print(f"You leveled up! You are now level {self.level}!")
        
    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= 10 * self.level:
            self.level_up()