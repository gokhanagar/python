# error => hata

# Error 
# print(a) => NameError
# int('1a3') => ValueError
# print(10/0) => ZeroDivisionError
# print('denem' e) => SyntaxErro




# error handling => hata yonetimi
# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)

# except (ZeroDivisionError,ValueError):
#     print('yanlis birgi girdiniz' )
    
   
while True: 
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)

    except Exception as ex:
        print('yanlis birgi girdiniz', ex )
    else:
        break;



















































