# Bankamatik uygulamasi

gokhanHesap = {
    'ad': 'gokhan ozturk',
    'hesapNo':'1234353',
    'bakiye':3000,
    'ekHesap':2000
}

gamzeHesap = {
    'ad': 'gamze Turan',
    'hesapNo':'987456',
    'bakiye':2000,
    'ekHesap':1000
}

def paraCek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print("paranizi alabilirsiniz")
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']
        
        if(toplam >= miktar):
            ekHesapKullanimi = input('ek hesap kullanilsin mui (e/h)')
            
            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('paranizi alabilirsiniz')
            else:
                print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} bulunmaktadir.")

        else:
            print('uzgunuz bakiye yetersiz')



paraCek(gamzeHesap,1000)
paraCek(gamzeHesap,2000)







