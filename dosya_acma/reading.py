# try:
#     file = open("newFile2.txt","r")
# except FileNotFoundError:
#     print("dosya okuma hatasi")    
# finally:
#     print("dosya kapandi")
#     file.close()



file = open("newFile.txt","r", encoding = "utf-8")

#for dongusu

# for i in file:
#     print(i, end = "")


# read()fonksiyonu

# content1 = file.read()

# print("icerik 1")
# print(content1)

# content2 = file.read()
# print("icerik 2")
# print(content2)
# file.close()


# content = file.read(5)
# content = file.read(3)
# content = file.read(2)
# print(content)


#************** readline() fonksiyonu
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")


#************** readlines() fonksiyonu
liste = file.readlines()

print(liste)
print(liste[0])


file.close()



















































