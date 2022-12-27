name = 'Mert'
surname ='Turna'
age = '36'

greeting = 'My name is ' + name + ' ' + surname + ' and \nI am ' + str(age) + ' years old'
legnth = len(greeting)

# print(greeting[0])
# print(greeting[3])
# print(len(greeting))

# print(greeting[legnth-1])
#print(greeting[-1])
#print(greeting[2:5])


#============================================================

name = 'Cinar'
surname = 'Can'
age = 23

# print('My name is {} {}'.format(name,surname))
#print('My name is {1} {0}' .format(name, surname))
#print('My name is {s} {n}' .format(n=name, s=surname))
#print("My name is {} {} and I'm {} years old".format(name,surname,age))

#result = 200 / 700
#print("result is {r:1.4}".format(r=result))

#print(f"My name is {name} {surname} and I'm {age} years old.")

#============================================================


website = "http://www.gokhanagar.com"
course = "Python Kursu: Bastan sonra python programlama rehberiniz (40 saat) "

# 1.soru
#print(len(course))
length = len(website)

# 2. soru
#print(website.replace('w', ""))
result = website[7::10]


# 3. soru
#print(website.replace("com", ""))
result = website[22:25]
result = website[length-3:length]

# 4. soru
#print(website[:16])
#print(website[-16:])

result = course[0:15]
result = course[:15]
result = course[-15::]

# 5. soru
#print(course[::-1])
result = course[::]

s="12345"
#print(s[::5])

name, surname, age, job = 'Bora', 'Yilmaz', 32, 'muhendis'

# 6.soru 
result = "Benim adim " + name + " " + surname + ", Yasim "+ str(age) + " ve meslegim " + job
result = "Benim adim {} {}, Yasim {}  ve meslegim {}".format(name,surname,age,job) 
#print(result)

# 7. soru
#"Hello world" ifadesindeki w harfini 'W' ile degistirin
s= "Hello world"
s = s.replace("w", "W")
#print(s)

































































