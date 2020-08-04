class Person:
    def __init__(self, name, email, phone):
         self.name = name
         self.email = email
         self.phone = phone

    def greet(self, other_person):
         print('Hello %s, I am %s!' % (other_person.name, self.name))

Sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
Jordon = Person("Jordon", "jordon@aol.com", "495-586-3456")

Sonny.greet(Jordon)
Jordon.greet(Sonny)

print("Here is the contact information for Sonny: " + Sonny.email, Sonny.phone)
print("Here is the contact information for Jordon: " + Jordon.email, Jordon.phone)

# print(Sonny.email, Sonny.phone, Jordon.email, Jordon.phone)