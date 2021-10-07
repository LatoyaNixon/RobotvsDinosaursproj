from weapon import Weapon


class Robots():
   def __init__(self, name, health, weapon, power):
    self.name = name
    self.health = 100
    self.weapon = weapon
    self.power_level = power()


    def ability_to_attack(self, dinosaur):
        pass


    def lose_health_points(self, dinosaur):
        pass

    
  