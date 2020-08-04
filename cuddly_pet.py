class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self. mopiness = mopiness


# """ Allows you to put a string on multiple lines """
 
    def __str__(self):
        return """
            %s:
            Fullness: %d
            Happiness: %d
            Hunger: %d
            Mopiness: %d
            """ % (self.name, self.fullness, self.happiness, self.hunger, self.mopiness)

    def be_alive(self):
        print("Be alive method for Pet Class")

guster = Pet("Guster", 50, 50 ,5, 0)
# print(guster)

class CuddlyPet(Pet):
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5, cuddle_level="Cuddly"):
        super().__init__(name, fullness, happiness, hunger, mopiness)
        self.cuddle_level = cuddle_level

# This __str__ overrides the parent class values. Used to add Cuddle Level to sub-class CuddlyPet.

    def __str__(self):
        return """
            %s:
            Fullness: %d
            Happiness: %d
            Cuddle Level: %s
            """ % (self.name, self.fullness, self.happiness, self.cuddle_level)

    def be_alive(self):
        super().be_alive()
        print("Be alive method for the Cuddly Pet Class")

beans = CuddlyPet("Beans", 10, 100, 200, 0, "Extra Cuddly")

# print(beans)

guster.be_alive()
beans.be_alive()