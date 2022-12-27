fruits = {'orange','apple','banana'}

#print(fruits[0]) indekslenemez

for x in fruits:
    print(x)

fruits.add('cherry')

#print(fruits)
fruits.update(['mango','grape'])
#print(fruits)

# myList = [1,2,5,4,4,2,1]
# print(myList)
# print(set(myList))

fruits.remove('mango')
fruits.discard('apple')
fruits.pop() # rastgele siler

#print(fruits)

#====================================================

x = 5
y =25

x = y
y = 10
#print(x,y)

a = ['apple','banana']
b = ['apple','banana']

a = b
b[0]='grape'

print(a,b)











































