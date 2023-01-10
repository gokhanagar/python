import random

# for i in range(10):
#     print(random.randint(1, 5))


#random.random() sifir ile bir arasindaki rastgele sayilar uretir
#random.uniform(10, 30) alt ve ust sinir arasinda rastgele sayilar uretir
#random.randint(1, 5) ust sinir dahil. Tam sayi ureten rastgele sayilar uretir
#random.randrange(10,20,2)

hak = 5
can = int(input("Bir sayi girin: "))
hak = can
rastgele_sayi = random.randint(1, 100)
x=0


while x < can:
    sayac +=1 
    girilen_sayi = int(input("1-100 arasinda sayi giriniz: "))
    hak -=1
    if rastgele_sayi == girilen_sayi:
        print(f"tebrikler {sayac}. defada bildiniz.Toplam puaaniniz:{100-(100/can)*(sayac-1)}")
        break
    elif rastgele_sayi>girilen_sayi:
        print("yukari")
    else:
        print("asagi")

    if hak ==0:
        print(f"hakkiniz bitti {rastgele_sayi}")

































































