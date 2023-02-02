liste = ["1","2","5a","10b","abc"]

# 1: Liste elemanlari icindeki sayisal degerleri bulunuz/
# toplam =0
# for item in liste:
#     if item.isdigit():
#         print(item)
#     else:
#         toplam += 1

# print(toplam)


# for x in liste:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue    

#2: Kullanici'q' degerini girmedikce aldiginiz her inputun sayisal deger
# oldugundan emin olunuz aksi halde hata mesaji yazin

# while True:
#     sayi = input("sayi: ")

#     if sayi == 'q':
#         break

#     try:
#         result = float(sayi)
#         print("girdiginiz sayi: ", result )
#     except ValueError:
#         print("gecersiz sayi")
#         continue


#3: girilen parola icindeki turkce karakter hatasi veriniz.

# def checkPassword(parola):

#     turkce_karakterler = 'şçöüğ'


#     for i in parola:
#         if i in turkce_karakterler:
#              raise TypeError('Parola turkce karakter iceremez')
#         else:
#              pass
# parola = input=('parola: ')
# print('gecerli parola')

# try:
#     checkPassword(parola)
# except TypeError as err:
#     print(err)        
        
        
        
        
#4: Faktoriyel fonksiyonu olusturup fonksiyona gelen deger icin hata mesaji verin

def faktoriyel(x):
    x = int(x)
    
    if x < 0:
        raise ValueError('Negatif deger')

    result = 1
    
    for i in range(1,x+1):
        result *=i
        
    return result


for x in [5,-3,4,20,'10a']:
    try:
        y = faktoriyel(x)     
    except ValueError as err:
        print(err)
        continue































































