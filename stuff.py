from player import Player
from enemy import Enemy
from battle import battle
import random

def main():
    name = input("Enter your character's name: ")
    player = Player(name)
    
    while player.hp > 0:
        print("\nWhat would you like to do?")
        print("1. Explore")
        print("2. Check Stats")
        print("3. Heal")
        print("4. Quit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            name = random.choice(['Goblin', 'Dragon', 'Dog', 'Pigeon'])
            hp = random.randint(30, 100)
            attack = random.randint(3, 15)
            enemy = Enemy(name, hp, attack)
            # goblin = Enemy("Goblin", 60, 5)
            battle(player, enemy)
        elif choice == '2':
            print(f"{player.name}'s stats")
            print(f"HP: {player.hp}")
            print(f"Attack: {player.attack}")
            print(f"Level: {player.level}")
            print(f"XP: {player.xp}")
        elif choice == '3':
            player.hp = player.full_hp
        elif choice == '4':
            break
        else:
            print("Invalid choice. Try again.")
            
main()
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
def battle(player, enemy):
    print(f"A wild {enemy.name} appears!")
    while player.hp > 0 and enemy.hp > 0:
        print(f"Your HP: {player.hp}")
        print(f"Enemy's HP: {enemy.hp}")
        action = input("Do you want to attack or run? ").lower()
        if action == 'a' or action == 'attack':
            player.attack_enemy(enemy)
            enemy.attack_player(player)
        elif action == 'r' or action == 'run':
            print("You ran away!")
            return

    if player.hp <= 0:
        print("You have been defeated...")
    else:
        print(f"You defeated {enemy.name}!")
        player.gain_xp(10)
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
    
