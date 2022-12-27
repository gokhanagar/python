# username, password => database

# 'gokhanagar' '123456'

a,b,c,d = 5,5,10,4

password = '1234'
username = 'gokhanagar'

result = (a == b) #True
result = (a == c) #False
 
result = ('gokhanagar' == username) # True
result = ( a != b) #False
result = ( a != c) # True
result = ( a > c) # False
result = ( a < c ) # True
result = ( a >= b) #True
result = (True == 1) #True
result = (False == 0) # True 

#=============================================================

# Soru 1
# num1 = int(input("num1: "))
# num2 = int(input("num2: "))

# result = num1 > num2
# result2 = num2 > num1
# print(result)
# print(result2)

# Soru 2
# num1 = int(input("num1: "))
# num2 = int(input("num2: "))
# num3 = int(input("num3: "))

# vize = ((num1 + num2)/2)*0.6
# final = (num3 * 0.4)
# ortalama = vize + final 

# if ortalama > 50:
#     print('gecti')


# Soru 3
# num1 = int(input("number: "))
# if num1 % 2 == 0:
#     print("sayi cifttir")
# else:
#     print('sayi tektir')


# Soru 4
# num1 = int(input("number: "))
# if num1>0:
#     print("sayi pozitif")
# else:
#     print('sayi negatif')


#=======================================================
x =5
hak = 5
devam = 'e'
result =  5 < x < 10

# and
result = (x > 5) and (x < 10)
result = (hak > 0) and (devam == 'e')

# or
result = (x > 0) or (x % 2 == 0)

# not
result = not(x > 0)

# x, 5-10 arasinda olan bir cift sayi mi?

# ============================================================================
#num = int(input('num: '))

# Soru 1
# if num >0 and num <100:
#     print('Sayi sifir ile 100 arasinda')

# Soru 2
# if num > 0 and num %2 == 0:
#     print(" Sayi pozitif bir cift sayidir")
# else:
#     print('Sayi pozitif veya cift degildir')

# Soru 3
# email = 'gokhanagar@gmail.com'
# password = '12345'

# girilenEmail = input('email: ')
# girilenSifre = input('sifre: ')

# if email == girilenEmail and password==girilenSifre:
#     print("bilgiler dogru")
# else:
#     print("bilgiler yanlis")
    

# Soru 4
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

result = (a > b) and (a > c)

# Soru 5
# vize1 = int(input("num1: "))
# vize2 = int(input("num2: "))
# final_sinav = int(input("num3: "))

# vize = ((vize1 + vize2)/2)*0.6
# final = (final_sinav * 0.4)
# ortalama = vize + final 
# print(ortalama)

# if ortalama >= 50 and final_sinav >= 50:
#     print('gecti')
# elif final_sinav > 70:
#     print('gecti')
# else:
#     print('kaldi')
    
# Soru 6
isim = input('isim: ')
kilo = float(input('kilo: '))
boy = int(input('boy: '))
result = kilo % boy **2
print(result)

if result>0 and result<18.4:
    print('zayif')
elif result>18.5 and result < 24.9:
    print('normal')
elif result>25 and result<29.9:
    print('fazla kilolu')
elif result>30 and result < 34.9:
    print('sisman')             














