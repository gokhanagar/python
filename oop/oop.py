# Object Oriented Programmin (oop)
# class 

class Person:

    #class attributes
    address = 'no information'    
    
    
    #constructor
    def __init__(self,name,year):
        self.name = name
        self.year = year
        print('init metodu calisti')
        
    # object attributes
    #instance methods
    def intro(self):
        print("hello there. I am " + self.name)
        
    #instance methods    
    def calculateAge(self):
        return 2019 - self.year    


#object ( instance )

p1 = Person("gokhan",1991)
print(p1.name)

p2 = Person("yagmur",1995)
print(p2)
print(type(p1))

#updating 
p1.name = 'ahmet'
p1.address = 'kocaeli'

#accessing object  attributes
print(f'name: {p1.name} year: {p1.year} address: {p1.address}')
print(f'name: {p2.name} year: {p2.year}')


p1.intro()
p2.intro()

print(f'adim: {p1.name} ve yasim: {p1.calculateAge()}')
print(f'adim: {p2.name} ve yasim: {p2.calculateAge()}')
















































