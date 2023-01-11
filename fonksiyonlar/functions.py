def sayHello(name = 'user'):
    return'Hello ' + name



msg = sayHello("cinar")
print(msg)


def total(num1,num2):
    return num1 + num2

result = total(10,20)
print(result)


def yasHesaplama(dogumYili):
    return 2019 - dogumYili

ageCinar = yasHesaplama(2017)
ageAda = yasHesaplama(2015)

print(ageAda)


def emekliligeKacYilKaldi(dogumYili, isim):
    yas = yasHesaplama(dogumYili)
    emeklilik = 65 - yas
    
    if emeklilik > 0:
        print(f'emekliliginize  {emeklilik} yil kaldi')
    else:
        print("zaten emekli oldunuz")

emekliligeKacYilKaldi(1983, 'burcu')
emekliligeKacYilKaldi(1950, 'yagmur')























































