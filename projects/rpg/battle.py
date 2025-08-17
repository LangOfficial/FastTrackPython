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
