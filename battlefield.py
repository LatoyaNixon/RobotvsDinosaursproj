from _typeshed import Self
from dinosaur import Dinosaur
from herd import Herd
from fleet import Fleet
from robot import Robots
from weapon import Weapon




class Battlefield():
    def __init__(self):
        self.fleet = Fleet()
        self.robot_one_turn = self.fleet.fleet_list[1]
        self.robot_two_turn = self.fleet.fleet_list[2]
        self.robot_three_turn = self.fleet.fleet_list[3]

        self.herd = Herd()
        self.dino_one_turn = self.fleet.fleet_list[1]
        self.dino_two_turn = self.fleet.fleet_list[2]
        self.dino_three_turn = self.fleet.fleet_list[3]
        self.dino_input = None
        self.robot_input = None
        
    def run_game(self):
        if(self.herd.herd_list) == 3 and(self.fleet.fleet_list) == 3:
            self.welcome()
        if(self.fleet.fleet_list) > 0:
            self.display_robots()

        self.choose_dino()
        self.choose_robot()
        self.battle()
        self.winner_of_battle()
        self.end_of_game()

        print("Welcome to robots vs dinosaur!")
     
    def display_dino(self):
        index = 0
        for each in self.herd.herd_list:
            print(f"{index} {each.type} Power level -{each.attach_power}")
            index += 1
     
    def choose_dino(self):
        self.dino_input = (input("/n Please select a Dinosaur\n"))
        for each in self.herd.herd_list:
            if each == self.herd.herd_list[self.dino_input]:
                return(self.herd.herd_list(self.dino_input.type))
             
                
    def display_robot(self):
        index = 0
        for each in self.fleet.fleet_list:
            print(f"{index} {each.type} Power level -{each.attach.power}")
            index +=1
        
    def choose_robot(self):
        self.robot_input = (input("/n Please select a Robot\n"))
        for each in self.fleet.fleet_list:
            if each == self.fleet.fleet_list[self.robot_input]:
                return(self.fleet.fleet_list(self.robot_input.type))

    def battle(self):
        pass




    def winner_of_battle(self):
        print("The winner has been declared")
        if (self.herd.herd_list != 0):
            print("The dinosaur has won the battle!")
        if (self.fleet.fleet_list != 0):
            print("The robot has won the battle!")
        
              






    



