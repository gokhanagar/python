# with  open("newFile.txt", "r+", encoding = "utf-8") as file:
#     file.seek(20)
#     file.write("deneme")
    
    
    
# with  open("newFile.txt", "r+", encoding = "utf-8") as file:
#     print(file.read()) 
    
    
# ***** Sayfa sonunda guncelleme **********
    
# with open("newFile.txt","a", encoding="utf-8") as file:
#     file.write("\nemel can")
    
# with  open("newFile.txt", "r", encoding = "utf-8") as file:
#      print(file.read())     
    
    
# ******* sayfa basinda guncelleme **************
    
# with open("newFile.txt","r+", encoding="utf-8") as file:
#     content = file.read()
#     content = "canan gur\n" + content  
#     file.seek(0)
#     file.write(content)
#     print(content)    
    
    
    
 # ********** Sayfa ortasinda guncellem *************
 
with open("newFile.txt","r+", encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(3, "yilmaz aygun\n")
    file.seek(0)
    file.writelines(liste)
    
    # for i in liste:
    #     file.write(i)
    
with open("newFile.txt","r", encoding="utf-8") as file:    
    print(file.read())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    