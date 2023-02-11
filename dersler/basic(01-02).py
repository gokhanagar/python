# x = 5
# # = ile atama yapılır. matematikteki eşitlik değildir. x variable na 5 değeri atanır. 

# #print(x)
# #print(x*6)

# y="hello"

# # string variable lar "" içinde yazılır
# print(y)

# print(x,y)

# # print()

# # bir fonksiyondur. () varsa fonksiyon olduğunu gösterir. içine parametreler alır. sep= ile parametreler arasında olmasını
# # istediğmiz karakteri yazarız. default değeri boşluktur

# print(x,y, sep="---")

# input()
# bu fonksiyon ile kullanıcıdan alınan bir değer bir variable olarak atanır

# name = input("adiniz nedir: ")
# print(name)

# kullanıcıdan aldığımız yaş bilgisinin iki katını ekrana yazdıran bir program yazalım

#yas = input("yasinizi giriniz: ")  # kullanıcıdan alınan değer string bir değer olduğu için yanyana yazdı 
# print(yas * 2)
#print(int(yas) * 2)


# kullanıcıdan alınan iki sayının ortalamasını bulma

# sayi1 = int(input("sayi 1 giriniz: "))
# sayi2 = int(input("sayi 2 giriniz: "))
# ortalama = (sayi1 + sayi2) /2
# print(ortalama)


# answer = 0

# for i in range(2):
#     x = input("please enter a number")
#     answer += int(x)
# print(answer / 2)     



# python indentation   

# bir alt satırın üst satırla ilişkili olduğunu göstermek için bir tab içerde yazılması, 
# bir iki yada üç boşlukta bırakılabilir ama ideal olan 1 tab boşluktur 

# if 6<10:
#     print("doğru")


# x,y,z="apple","banana","cherry"
# print(x)
# print(y)
# print(z)


# fruits = ["apple","banana","cherry"]
# x,y,z = fruits
# print(x)
# print(y)
# print(z)


# sequential steps   

# kod satırları yukardan aşağıya sırasıyla çalışsır

# x=2
# print(x)
# x=x+2
# print(x)



# conditional steps   
# kod satırları şarta bağlı olarak çalışır

# x=5
# if x<10:
#     print("smaller")
    
# if x>20:
#     print("bigger")
    
# print("finish")


# repeated steps
# bir koşula bağlı olarak tekrar eden döngüsel bir şekilde çalışır


# n=5
# while n>0:
#     print(n)
#     n=n-1
    
# print("blastoff!")


# resorved words
"""
false, class, return, is, finally, None, if, for, lambda, continue,
True, def, from, while, nonlocal, and, del, global, not, with, 
as, elif, try, or, yield, assert, import, pass, break, in, raise, except
"""


# sentences or lines
"""
x=2          assignment statement
x=x+2        assignment with expression
print(x)     print statement
"""


# sequence types 

    # list : [] içerisinde yazılır. list tipindeki bir data içerisinde list, tuple, dictionary yada string gibi farklı tiplerde 
    #        eleman barındırabilir. mutable özelliktedir        
    
    # tuple : () içerisinde yazılır. tuple tipindeki bir data içerisinde list, tuple, dictionary yada string gibi farklı tiplerde 
    #        eleman barındırabilir. immutable özelliktedir 
    
    
# x= ["apple", "banana", "cherry"]
# y= ("apple", "banana", "cherry")
# print(type(x))
# print(type(y))


# map type : dictionary (dict)

# {} içeriisnde yazılırlar. key ve value değerleri olur. mutable özelliktedir
# x= {"name": "john", "age": 30}
# print(type(x))


# set type : set

    # {} içerisnde yazılırlar. mutable özelliktedir, matematikteki kümeler mantığında çalışır. 
    # duplicate olmaz benzer elemanlardan birkac tane içermez.değişken tanımlanırken birkaç defa yazılabilir fakat sonuc olarak
    # duplicate içermeyen sonuc döndürülür
    
# x= {"apple", "banana", "cherry"}
# print(type(x))
    
# x1= {"apple", "banana", "cherry", "apple", "banana", "cherry", "apple", "banana", "cherry"}
# print(x1)    
    
    
    
#bos_set= set()                      # boş bir set türünde değişken tanımlamak istersek set() şeklinde tanımlarız. normalde 
                                    # set ler {} ile yazılır buna dikkat    
    
    
    
 # boolean type : bool

# True/False değerlerinin atandığı deişkenlerden oluşan veri tipleri. immutable özelliktedir.   
    
# x=True
# print(type(x))    
    
    
"""

    bir datanın içerisinde yer alan elaman değiştirilebiliyorsa mutable dır. değiştirilemiyorsa immutable dır
    
    
immutable                         mutable

-string                           -list
-tuple                            -dictionary
-frozenset                        -set
-boolean
-number
  -integer
  -float
  -long integer
  -complex
"""    
    
    
    
    
    
    
    
    
    
    
    
    




