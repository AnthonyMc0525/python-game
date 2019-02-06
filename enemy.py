from random import randint

class Enemy(object):
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.damage = 20
        
    def is_alive(self):
        return self.hp > 0

    def attack(self):
        return self.damage
 
    def take_damage(self, amount):
        self.hp -= amount
        return self.hp 
