# In-class exercise to practice making classes in Python.

class Car:

    def __init__(self, owner, make, model, year):
        self.owner = owner
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return "%s owns a %s %s from %d." % (self.owner, self.make, self.model, self.year)
    
    # Instance Method
    def color(self, color):
        self.color = color
        return "The %s is %s." % (self.make, self.color)

Harmony = Car("Harmony", "Kia", "Sportage", 2019)
Sean = Car("Sean", "VW", "Golf", 2018)

print(Harmony)
print(Sean)

print(Harmony.color("Grey"))
print(Sean.color("Purple"))
