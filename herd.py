from dinosaur import Dinosaur

class Herd():
    def __init__(self):
        self.herd_list = []
        self.create_herd()

    def create_herd(self):
        spinosaurus = Dinosaur("Spinosaurus, 24, 100")
        raptor = Dinosaur("Raptor, 20, 80")
        styracosaurs = Dinosaur("Styracosaurs, 25, 75")
        self.herd_list.append(spinosaurus)
        self.herd_list.append(raptor)
        self.herd_list.append(styracosaurs)
        