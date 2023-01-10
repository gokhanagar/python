# x = 5
# y = 10
# z = 20

x,y,z = 5,10,20
#x,y = y,x
x = x + 5
x += 5
x -= 5
x /= 5
x //= 5
x %= 5
y **= 5

values = 1,2,3,4,5
# print(values)
# print(type(values))

x,y, *z = values

# print(x,y,z)

#===========================================================

x, y, z = 2, 5, 10

numbers = 1,5,7,10,6

# Soru 1
# num1 = input('number1: ')
# num2 = input('number2: ')
# num3 = int(input('number3: '))


# result = (int(num1)*int(num2)) - (x+y+z)
# print(result)

# Soru 2 kalansiz bolumu nedir
result = y // x
#print(result)

# Soru 3 mod 3'u nedir
toplam = (x+y+z)
result = toplam % 3
#print(result)

# Soru 4
result = y ** x
#print(result)


# Soru 5 z'nin kupunu alin
x, *y, z = numbers
result = z **3
#print(result)


# Soru 6
x, *y, z = numbers

#result = y[0] + y[1] + y[2]
#print(result)

sum = 0
for x in y:
    sum +=x
    
#print(sum)    

#===============================================================================
















