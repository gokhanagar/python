# global scope
x = 'global x'

# def function():
#     x = 'local x'
    
# function()
# print(x)

#=============================================

# name = 'burcu'

# def changeName(new_name):
#     name = new_name
#     print(name)
    
# changeName('ada')
# print(name)    

#====================================================

name = 'global string'

def greeting():
    name = 'cinar'

    def hello():
        print('hello' + name)

    hello()

greeting()

#=============================================================


















