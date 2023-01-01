import datetime

isLoggedin = False

# if isLoggedin :
#     print('hosgeldiniz')


# x = 10
# y = 20

# if x > y:
#     print(' x y den buyuk')
# else:
#     print('y x den buyuk')
    
    
# Soru 1 
# name = input('isim: ')
# yas = int(input('yas: '))
# egitim = input('egitim_durumu:')

# if yas>= 18 and egitim == 'universite':
#     print('ehliyet alabilirsin')
# elif yas>= 18 and egitim == 'lise':
#     print('ehliyet alabilirsin')
# else:
#     print('ehliyet alamazsin')

# Soru 2
# vize1 = int(input("vize1: "))
# vize2 = int(input("vize2: "))
# final = int(input("final: "))

# result= ((vize1 + vize2)/2 + final)/2
# print(result)

# if result>=0 and result <= 24:
#     print('0')
# elif result>=25 and result <= 44:
#     print('1')
# elif result>=45 and result <= 54:
#     print('2')
# elif result>=55 and result <= 69:
#     print('3') 
# elif result>=70 and result <= 84:
#     print('4') 
# elif result>=85 and resul <= 100:
#     print('5')  
# else:
#     print("yanlis deger girdiniz")
  
gvr = datetime.date(1956,1,31)
#print(gvr)

td = datetime.date.today()
#print(td.day)
#print(td.weekday())

tdelta = datetime.timedelta(days=7)
#print(td - tdelta)

#date2 = date1 + timedelta
# timedelta = date1 + date2

bday = datetime.date(2016,9,24)
till_bday = bday - td
#print(till_bday)


# Soru 3
# Trafige cikis tarihi alinan bir aracin servis zamanini asagidaki bilgilere gore hesaplayiniz
#1. bakim => 1. yil
#2. bakim => 2. yil
#3. bakim => 3. yil
# simdi - 2018/7/6 => gun 

tarih = input('araciniz hangi tarihte trafige cikti(2019/8/9): ')
tarih = tarih.split('/')

# print(tarih)
# print(tarih[0])
# print(tarih[1])
# print(tarih[2])

trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCikis
days = fark.days

if days<= 365:
    print('1. servis araligi')
elif days > 365 and days <= 365*2:
    print('2. servis araligi')
elif days > 365*2 and days <= 365*3:
    print('3. servis araligi')   
else:
    print('hatali sure')





































































