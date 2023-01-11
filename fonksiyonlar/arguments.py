# def changeName(n):
#     n = 'ada'
    
#     name = ' yigit'
    
#     changeName(name)
    
    
# def change(n):
#     n[0]='istanbul'
        
# sehirler = ['ankara','izmir']
    
# change(sehirler)
    
# print(sehirler)    
    
    
    
# def add(a,b,c=0):
#     return sum((a,b,c))    
    
# print(add(10,20,30))    
    
    
# def add(*params):
#   print(type(params))
#     sum = 0 
    
#     for n in params:
#         sum += n
#     return sum

#print(add(10,20,30))    
    
# def displayUser(**args): # **args dictionary
#     print(type(args))
#     for key, value in args.items():
#         print('{} is {}'.format(key,value))        
        
        
# displayUser(name= 'cinar', age =2, city= 'istanbul')
# displayUser(name= 'ada', age =12, city= 'kocaeli',phone='1123123')    
# displayUser(name= 'yigit', age =14, city= 'antalya',phone='11234323',email="sdf@gmail.com")       
    
def myFunc(a,b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    
myFunc(10, 20,30,40,50, key1 = 'value1', key2='value2')    
    
    
    
    
    
    
