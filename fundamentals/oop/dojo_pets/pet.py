class Pet:
    def __init__(self, name , type , tricks ):
        self.name = name
        self.type = type
        self.tricks = tricks
        self. health = 100
        self.energy = 100

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.health += 20
        self.energy += 5
        return self


    def play(self):
        self.health += 5
        return self

    
    def noise(self):
        print("schooby dooby dooooo!!")
        return self