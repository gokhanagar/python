mylist = [1,2,3]
# myString='my string'

# print(len(mylist))
# print(len(myString))

class Movie():
    def __init__(self, title, direction,  duration):
        self.title = title
        self.direction = direction
        self.duration = duration
        print('movie objesi olusturuldu')
        
    def __str__(self):
        return f"{self.title} by {self.direction}"   
        
    def __len__(self):
        return self.duration   
    
    def __del__(self):
        print("film silindi") 

m = Movie('film adi', 'yonetmen adi', 120)



# print(type(m))
# print(str(m))

print(len(mylist))
print(len(m))

del m

print(m)












































