from random import randint
from jobs import Job


class Player(object):
    def __init__(self):
        self.name = input('What is your name? ')
        self.hp = 100
        self.job = ''
        self.victory = False

    def is_alive(self):
        return self.hp > 0

    def attack(self):
        damage = randint(0, 40)
        return damage

    def take_damage(self, amount):
        self.hp -= amount
        return self

    #def use_skill(self, skill_name):
       # skill_name in self.job.skills:
            
