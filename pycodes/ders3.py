"""
for i in [1,2,3,4,5,6,7,8,9,10]:
    print(i)
"""

"""
for i in range(10):
    print(i+1)
"""

"""
for i in range(1,11):
    if i == 0:
        print("Sen yoksun!")
    elif i % 2 == 0:
        print(i, "bir çift sayıdır")
    else:
        print(i, "bir tek sayıdır")
"""


from time import sleep

"""
for i in range(10):
    print(i)
    sleep(1)

"""

"""
for i in reversed(range(1,4)):
    print(i)
    sleep(1)

for i in range(4):
    print("bi bi bi bip")
    sleep(1)



"""

"""
counter = 1

while counter <= 10:
    print(counter)
    counter += 1

"""



"""
from time import sleep

counter = 10

while counter > 0:
    print("bip bip", "kalan süre:", counter)
    sleep(1) 
    counter -= 1

print("güüüÜÜÜÜüüüüm")

"""
"""
from random import randint
yaprak_sayisi = randint(15,22)

son_durum = 'seviyor'

while yaprak_sayisi >= 0:
    print('yaprak sayısı: ',yaprak_sayisi, ' : ',son_durum)
    sleep(.5)
    #### Durumu tersine çevir
    if son_durum == 'seviyor':
        son_durum = 'sevmiyor'
    else:
        son_durum = 'seviyor'
    ####
    yaprak_sayisi -= 1


if son_durum != 'seviyor':
    print('cok da sey etme, papatya fali neticede')
else:
    print('nihahahahaha, sevmiyormuş!!!!')

"""
"""
from random import randint, SystemRandom
secure_random = SystemRandom()

sevmiyor_listesi = ['yok be %s sana bakmaz', 'hadi be ordan', "lan porsche'u var diyorum", 'cok da sey etme']
seviyor_listesi  = ['çok da şey etme, papatya falı sonuçta', 'kullanıp atar o seni, salma kendini', 'bak versacesi yok diyorum',
                   "porsche'u ikinci el diyorlar"]

yaprak_sayisi = randint(15,22)

son_durum = 'seviyor'

yar = input('yarinizin ismini giriniz: ')
print('%s için papatya falı başlatılıyor' % yar)
while yaprak_sayisi > 0:
    print('yaprak sayısı: ',yaprak_sayisi, ' : ',son_durum)
    sleep(.5)
    #### Durumu tersine çevir
    if son_durum == 'seviyor':
        son_durum = 'sevmiyor'
    else:
        son_durum = 'seviyor'
    ####
    yaprak_sayisi -= 1

if son_durum != 'seviyor':
    output = secure_random.choice(seviyor_listesi)
else:
    output = secure_random.choice(sevmiyor_listesi)
    if '%s' in output:
        output = output % yar
print(output)

"""
"""
####################################################

while True:
    sayi = input('sayı giriniz: ')
    if sayi.lower() == 'dur':
        break
    else:
        sayi = float(sayi)
        print(sayi**2)
"""
"""
from time import sleep

sabir_katsayisi = 3
counter = 0
while True:
    if counter >= sabir_katsayisi:
        print("Pat")
        sleep(.5)
        print("Güm")
        sleep(.5)
        print("Çotank")
        sleep(.5)
        print("Tamam tamam kızma")
        break
    cevap = input("Sana deniz anası takidi yapayım mı? ")
    cevap2 = "öyle %s demekle olmaz" % cevap
    print(cevap2)
    counter += 1
    print(counter)


"""


