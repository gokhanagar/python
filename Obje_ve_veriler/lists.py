#my_list = [1,2,3]
#my_list = ["bir",2,True,5.6]
#print(my_list)

list1 = ['one' ,'two','three']
list2 = ['four','five','six']

numbers = list1 + list2
#print(numbers)
#print(len(numbers))

userA = ['Can',36]
userB = ["beyza", 25]

users = userA + userB
#print(users)

users = [userA, userB]
#print(users[1][0])

#================================================================

# Soru 1
list = ['Bmw','Mercedes','Opel','Mazda']
arabalar = ['Bmw','Mercedes','Opel','Mazda']
#print(result)

# Soru 2 
result = len(list)
result = len(arabalar)

#print(result)

# Soru 3
#print(list[0])
#print(list[result-1])
result = arabalar[-1]

# Soru 4
list[3] = "toyota"
#print(list)
arabalar[-1] = "Toyota"

# Soru 5
#print(list.index("Mercedes"))
result = "Mercedes" in arabalar
#print(result)

# Soru 6
#print(list[-2])
result = arabalar[-2]

# Soru 7
#print(list[:3])
result = arabalar[0:3]
result = arabalar[-2:]

# Soru 8
list[3:] = "Toyota","Renault"
arabalar[-2:] =["Toyota","Renault"]


# Soru 9
list.append("Audi")
list.append("Nissan")
#print(list)

result = arabalar + ["Auid","Nissan"]

# Soru 10
list.remove(list[-1])
#print(list)

# Soru 11
list.reverse()
#print(list)



# Soru 12
studentA = ["Yigit", "Bilgi", 2010,[70,60,70]]
studentB = ["Sena","turan",1999,[80,70,90]]
studentC = ["Ahmet","Gokturk",1998,[80,70,60]]

#====================================================================================

numbers = [1,10,5,16,4,9,10]
letters = ['a','g','s','b','y','a','s']

val = min(numbers)
val = max(numbers)
val = max(letters)
val = min(letters)

val = numbers[3:6]
val = numbers[:3]
val = numbers[4:]
numbers[4] = 40
numbers.append(49)
#numbers.pop()
#numbers.pop(0)
#numbers.remove(49)

numbers.sort()
letters.sort()
#print(letters)

#print(numbers.count(10))
#print(letters.count("a"))


#==================================================================

names = ["ali", 'yagmur', 'hakan', 'deniz']
years = [1998,2000, 1998, 1987]

# Soru 1
names.append('cenk')

# Soru 2
names.insert(0, 'sena')

# Soru 3
names.remove('deniz')

# Soru 4
#names.index('deniz')

# Soru 5
result = names.index('ali')
result = 'ali' in names
result = names.index('ali')

# Soru 6
names.reverse()

# Soru 7
names.sort()

# Soru 8
years.sort()

# Soru 9
str = 'chevrolet,dacia'
#liste = []
liste = str.split(",")

#print(liste)

# Soru 10
min_value = min(years)
max_value = max(years)

#print(max_value)

# Soru 11
print(years.count(1998))

# Soru 12
years.clear()
#print(years)

# Soru 13
markalar = []
marka = input("marka: " )
markalar.append(marka)
marka2 = input("marka: " )
markalar.append(marka2)
marka3 = input("marka: " )
markalar.append(marka3)


print(markalar)











































