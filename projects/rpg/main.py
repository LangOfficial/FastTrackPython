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