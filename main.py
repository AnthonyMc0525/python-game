from enemy import Enemy

from player import Player
from jobs import Job
import time

print("""
 ___________________________________________
|                                           |
|         'WELCOME ADVENTURER!'             |
|                                           |
|  ' You have been dropped into a pit. You  |
|   dont remember anything except you were  |
|   surrounded by a group of thugs'         |
|                                           |
|                                           |
|                                           |
|                                           |
|                                           |
 -------------------------------------------
        """)
time.sleep(3)

player = Player()
print(f"Welcome {player.name}")
job_choice = input('what class would you like? "black mage" or "paladin" ')
job = Job(job_choice)
player.job = job

enemy = Enemy('enemy')

def battle():
    print('an adversary is jumps in front of you, ready to strike. Not to fear though because due to your tuned senses you noticed it, and are ready')
    while (not player.victory and player.is_alive()):
        choice = input('Will you attack it? y or n: ') 
        if (choice =='y'):
            damage = player.attack()
            print(f"you have dealt {damage} damage")
            enemy.take_damage(damage) 
            time.sleep(1)
            print('the enemy strikes you back in a fit of rage')
            time.sleep(1)
            edamage = enemy.attack()
            print(f"the enemy has dealt {edamage} damage")
            player.take_damage(edamage)
            if enemy.hp <= 0:
                player.victory = True
                print('you have one the day adventurer!')

        elif choice == 'n':
            print('wrong choice!')
            time.sleep(1)
            edamage = enemy.attack()
            print(f"the enemy has dealt {edamage} damage")
            player.take_damage(edamage)
            if player.hp <= 0:
                print('you have been slain')
        else:
            print('not an option')
            time.sleep(1)
    

battle()























