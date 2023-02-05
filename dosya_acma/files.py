# Dosya acmak ve olusturmak icin open() fonksiyonu kullanilir
#Kullanimi: open(dosya_adi, dosya_erisme_modu)
#dosya_erisme_modu => dosyayi hangi amacla actigimizi belirtir

# "w": (Write) yazma modu. Dosyayi konumda olusturur.
#   ** dosyayi konumda olusturur.
#   ** dosya icerigini siler ve yeniden ekleme yapar.
 
# file = open("newfile.txt","w")
# file.close()

# file = open("C:/Users/gokha/python/newFile.txt","w")
# file.close()

# file = open("newFile.txt","w",encoding= "utf-8")
# file.write("gokhan agar")
# file.close()





# "a": (Append) ekleme. Dosya konumda yoksa olusturur.

# file = open("newFile.txt","a",encoding= "utf-8")
# file.write("\ngokhan agar")
# file.close()





# "x": (Create) olusturma. Dosya zaten varsa hata verir

# file = open("newFile2.txt","x",encoding= "utf-8")






# "r" (Read) okuma. varsayilan. dosya konumda yoksa hata verir.

file = open("newFile.txt", "r")

print(file)
























































