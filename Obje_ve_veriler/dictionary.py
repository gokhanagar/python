# key - value

# 41 =? kocaeli  34 => istanbul

sehirler = ['kocaeli','istanbul']
plakalar = [41,34]

#print(plakalar[sehirler.index('kocaeli')])


#print(plakalar['kocaeli'])  => 41
#print(plakalar['istanbul']) =>34

plakalar = {'kocaeli': 41 , 'istanbul':34}
#print(plakalar['kocaeli'])
#print(plakalar['istanbul'])

plakalar['ankara'] = 6
plakalar['kocaeli'] = 'new value'

#=========================================

users = {'gokhanagar' :
    {'age':32,
     'roles':['admin','user'],
     'email': 'gokhanagar@gmail.com',
     'address':'kocaeli',
     'phone':123123
     }, 
    'beyzaturan': {
      'age':23,
     'email': 'beyzaturan@gmail.com',
     'address':'istanbul',
     'phone':123423
     }
    }

#print(users['gokhanagar']['age'])
#print(users['beyzaturan']['address'])
#print(users['gokhanagar']['roles'])

#===============================================================

ogrenciler = {
    '120':{
        'ad':'ali',
        'soyad':'yilmaz',
        'telefon': '532 678 66 37'
    },
    '125':{
        'ad':'can',
        'soyad':'korkmaz',
        'telefon': '532 239 66 37'
    },
    '128':{
        'ad':'volkan',
        'soyad':'yukselen',
        'telefon': '532 678 12 37'
    }
  }

ogrenciler = {}

number = input("ogrenci no: ")
name = input("ogrenci adi: ")
surname = input("ogrenci soyad: ")
phone = input("ogrenci telefon: ")

ogrenciler[number] = {
    'ad' : name,
    'soyad' : surname,
    'telefon' : phone
}

ogrenciler.update(
    {
        number:{
            'ad':name,
            'soyad':surname,
            'telefon':phone
        }
    }
)


ogrNo = input('ogrenci no: ')
ogrenci = ogrenciler[number]

print(ogrenci)






















































































