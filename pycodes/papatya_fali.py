from random import randint, sample, shuffle, choice
from time import sleep

isim = input("yarinizin ismini giriniz: ")
sleep(1)
print("%s için papatya falı başlatılıyor:" % isim)
sleep(1)

yaprak_sayisi = randint(20,30)
son_durum = ''

for i in range(0,yaprak_sayisi):
    if i % 2 == 0:
        son_durum='seviyor'
        print(son_durum)
        sleep(.5)
    else:
        son_durum = 'sevmiyor'
        print(son_durum)
        sleep(.5)

if son_durum=='sevmiyor':
    print("%s seni sevmiyor!! Ahahahahahha" % isim)
else:
    print("papatya falı işte, çok da şey etme")

