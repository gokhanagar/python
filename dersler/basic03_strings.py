x= "hello"            # bir değişkene string bir ifade tanımlama

# len() fonksiyonu print() ve input() gibi bir builtin function dır. tüm data tipleri için kullanılır. 
# içerisinde yer alan string değişkenin karakter sayısını döndürür
# lenght den geliyor

len(x)
#print(len(x))

myList=["hello", 1, 1.5, False, [5,6,7]]
#print(len(myList))


# Access elements of the string
# Bir string değişkenin içerisinde belirli nokta, harf ve karaktere ulaşmak için kullanılır
# String değerin arka planda tutulan index değerlerine göre işlem yapar. istenilen index teki elemanı döndürür
# indexler soldan sağa 0 dan başlar 0,1,2,3... devam eder, sağdan sola -1 den başlar ...,-3,-2,-1 olarak devam eder

x="Hello World!"
print(x[0])

myString="Hi, how are you?"
SonHarf = myString[-1]                     # myString in -1 index değeri SonHarf değişkenine atanmış oldu
#print(SonHarf)



myString[len(myString)-1]   # myString değişkeninin son index değerine ulaşmak için len() değerinden 1 cıkarılır
                            # index ler 0 dan başlar. len() ise uzunluğu karakter sayısını verir, len() index ten 1 fazla olur 


print("hello"[2] )


#Slicing Strings
# Bir string değişkenin içerisinde belirli bir aralığa ulaşmak için kullanılır
# String değerin arka planda tutulan index değerlerine göre işlem yapar. 
# istenilen index değerler arasında yer alan elemanları döndürür. . 
# [start : stop] mantığı ile çalışır. start değeri dahildir stop değeri dahil değildir
# index ler soldan sağa 0 dan başlar 0,1,2,3... devam eder, sağdan sola -1 den başlar ...,-3,-2,-1 olarak devam eder


x="Hello World!"

x[3:8]            # 3üncü index değer olan l den (dahil) başlar ve 8inci index değer olan r ye (dahil değil) kadar olanları alır
x[:8]             # start yazılmazsa 0 index den başlar ve 8inci index değer olan r ye (dahil değil) kadar olanları alır
x[3:]             # stop yazılmazsa 3üncü index değer olan l den (dahil) başlar ve sona kadar olanları alır

myString="Apple Banana Cherry"
myString[:5]
myString[6:12]
print(myString[:])

# string[1:9:2]          # 1 index ten başlar 9 index e kadar gider 2 adımla
# string[::3]            # baştan sona 3 adımla gider. 0 index i yazar 3 index i yazar 6 index i yazar bu şekilde sona kadar gider


slice(-4,-1)           # slice() ile sabit bir dilimleme yöntemi belirlenir. sonrasında istenilen tüm değişkenlerde 
                       # bu dilimleme yöntemi kulanılarak işlem yapılır
                       # burda start stop yazılırken arada virgül var buna dikkat. 
                       # shift+tab ile parametrelere bak
                       
                       
                       
#========================================================================================================================================                       
# Strings methods 
# methodlar aynı zamanda birer fonksiyondur. bir DATA TİPİNE BAĞLI olarak çalışırlar. 
# her metod fonksiyondur fakat her fonksiyon metod değildir
# string metodlar, string bir değerin kendisi yada string bir değişkene bağlı olarak çalışırlar

# STRING.upper() / STRING.lower() 

# string değişkenin tüm elemanlarını büyük harf yapar (string.upper())
# string değişkenin tüm elemanlarını küçük harf yapar (string.lower())

x="Hello World!"
x.upper()

"Merhaba Dünya!".upper()
y='HELLO WORLD!'
y.lower()

'HELLO WORLD!'.lower()
'HELLO WORLD!'[-6:].lower()


str1="hello"
str1.upper()
str1            # methodlar string değeri değiştirmez. değişiklik olması yeni bir değişkene atama (asignment) yapılması gerekir

newstr=str1.upper()
# STRING.swapcase() 

# string değişkenin küçük harflerini büyük, büyük harflerini küçük yapar
"thiS iS A penCİL".swapcase()


# kullanıcıdan alınan ismin tüm harflerini büyük harf yapıp ekrana basan kodu yazın
# name=input("isim giriniz")
# print(name.upper())


# STRING.title() 

# string değişken içerisindeki her kelimenin baş harflerini büyük yapar
# print("this is s pencil".title())

# STRING.capitalize() 

# string değişkenin sadece baş harfini büyük yapar
# print("this is s pencil".capitalize())


# STRING.strip()       STRING.rstrip() / STRING.lstrip()

# string değişkenin sağda ve solda yer alan boşlukları siler. (soymak anlamına gelir)
# default değer boşluktur, boşlukları siler. parametre girilirse onu siler
# STRING.rstrip() sadece sağ tarafı siler
# STRING.lstrip() sadece sol tarafı siler


x="    Hello World!     "
#print(x.strip())


# y="aaaaHello World!aaaa"
# print(y.strip("a").upper())
# print(y.rstrip("a"))
# print(y.lstrip("a"))



# STRING.split()

# string değişkeni içerisinde yer alan parametreden bölerek liste tipinde döndürür
# default değer boşluktur birşey yazılmazsa boşluktan böler.


x="Hello World!"
print(x.split())
print(x.split("o"))

# STRING.replace()

# (oldvalue,newvalue,count) parametreleri verilir. eski değeri yeni değerle değiştirir. count değeri yazılırsa o kadar yapar 
# bu değişikliği. yazılmazsa default değer -1 dir yani tüm değerler için yapar

x="Hello World!"
# print(x.replace("e","oooo"))   # default değer -1. tüm "e" lerin yerine "oooo" yazar
# print(x.replace("l","oooo",2)) # count=2 olduğu için ilk 2 "l" değeri yerine "oooo" yazar
x.replace("l","oooo")              # default değer -1. tüm "l" lerin yerine "oooo" yazar



string="muccratccakbbca"
print(string.replace("cc","").replace("b",""))


# basit bir kriptolama
sifreleyici=str.maketrans("aiouhe","&5+^?=")     
# str.maketrans() metodu ile ilk parametredeki değerler yerine ikinci parametredeki değerler yazılır


password="hello world"
kriptolupassword=password.translate(sifreleyici)
print(kriptolupassword)

sifrecozucu=str.maketrans("&5+^?=","aiouhe")
cozulenpassword=kriptolupassword.translate(sifrecozucu)
print(cozulenpassword)



































