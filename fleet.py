from robot import Robot

class Fleet():
    def __init__(self):
        self.fleet_list = []
        self.create_fleet()

    def create_fleet(self):
        falcon = Robot("Falcon, 100")
        grim = Robot("Grim, 75")
        duck = Robot("Duck, 83")
        self.fleet_list.append(falcon)
        self.fleet_list.append(grim)
        self.fleet_list.append(duck)
        
        
