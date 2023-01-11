# 1-Gonderilen bir kelimeyi belirtilen kez ekranda gosteren fonksiyonu yazin

# def yazdir(kelime,adet):
#     print(kelime * adet)

# yazdir('merhaba\n', 5)

#2 - Kendisinie gonderilen sinirsiz sayidaki parametreyi bir listeye ceviren fonksiyonu yazin

# def listeyeCevir(*params):
#     liste = []
#     for param in params:
#         liste.append(param)
#     return liste

# result = listeyeCevir(10,2,3,4,5,6,7)

# print(result)

# 3- Gonderilen 2 sayi arasindaki tum asal sayilari bulun

# def asal_sayi_bul(num1,num2):
#     for sayi in range(num1, num2+1):
#         if sayi>1:
#             for i in range(2, sayi):
#                 if (sayi % i) ==0:
#                     break;
#             else:
#                 print(sayi)       


# print(asal_sayi_bul(10, 20))

# 4- Kendisinie gonderilen bir sayinin tam bolenlerini bir liste

def tamBolenListesi(num1):
    list = []
    for i in range(1, num1+1):
        if num1 % i ==0:
            list.append(i)
    print(list)

tamBolenListesi(10)





























































