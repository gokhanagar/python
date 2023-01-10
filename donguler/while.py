# 1-100 e kadar

# x=1

# while x <100:
#     if x % 2 ==1:
#         print(f"sayi tek {x}")
#     else:
#         print(f'sayi cift {x}')    
#     x +=1


# print("bitti")


# name = '' # false

# while not name.strip(): # bastan ve sondan bosluklari alir
#     name = input('isminizi giriniz: ')

# print(f'merhaba {name}')

#sayilar = [1,3,5,7,9,12,19,21]

# Soru 1

# index = 0
# while (index < len(sayilar)):
#     print("index: " , index, "sayi: " , (sayilar[index]))
#     index += 1
    
 # Soru 2   
# baslangic =  int(input("baslangic sayisi girin: "))
# bitis = int(input("bitis sayisi girin: "))
# i = baslangic

# while i < bitis:
#     if i % 2 ==1:
#         print(i)
#     i +=1

# Soru 3
# x= 1
# y = 100

# while x < y:
#     print(y)
#     y -= 1


# Soru 4
# x = 0
# liste = []
# while x < 5:
#     z = int(input("Bir sayi giriniz: "))
#     liste.append(z)
#     x +=1
# liste.sort()
# print(liste)    



# Soru 5

# urunler = []

# adet = int(input("kac urun eklemek istiyorsunuz: "))

# i =0

# while (i < adet):
#     name = input("urun ismi: ")
#     price = input("urun fiyati: ")
#     urunler.append({
#         'name':name,
#         'price':price
#     })
#     i +=1

#     for urun in urunler:
#         print(f'urun adi: {urun["name"]} urun fiyati: {urun["price"]}')

#==================================================================================================

# name = "beyza narin"

# for letter in name:
#     if letter == 'i':
#         continue
#     print(letter)


# x = 0

# while x < 5:
#     x +=1
#     if x ==2:
#         continue
#     print(x)
    

# 1 - 100 e kadar tek sayilarin toplami

# x = 0
# toplam = 0
# while x <= 100:
#     x +=1 
#     if x % 2 ==1:
#         toplam += x
      
# print(toplam)        


#=============================================================================
#range
# liste = [1,2,3]

# for item in range(50,100,10):
#     print(item)


# print(list(range(50,100,10)))

# enumarate
#index= 0
# greeting = "Hello there"

# # for letter in greeting:
# #     print(f"letter: {index} letter: {greeting[index]}")
# #     index +=1

# for index,item in enumerate(greeting):
#     #print(item)
#     print(f"index: {index} letter: {item}")
 

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']


#print(list(zip(list1,list2)))

# for item in (zip(list1,list2)):
#     print(item)






























