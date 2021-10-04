# Inheritance

#Parent class
class Person:
    def __init__(self, name, contact):
         self.name = name
         self.contact = contact

    def address(self):
        print(self.name, self.contact)  
        

#Child class
class Doctor(Person):
    pass

#Child class
class Patient(Person):
    pass


doc1 = Doctor("vishnu", 54848554)
pat1= Patient("athul", 454554157)


doc1.address()
pat1.address()