# def usalma(number):
   


#     def inner(power):
#         return number ** power

#     return inner


# two = usalma(2)

# print(two(3))





def yetki_sorgula(page):
    def inner(role):
        if role == 'Admin':
            return "{0} rolunun {1} sayfasina ulasabilir.".format(role,page)
        else:
            return "{0} rolu {1} sayfasina ulasamaz.".format(role,page)
    return inner

user1 = yetki_sorgula("product Edit")
print(user1("Admin"))































