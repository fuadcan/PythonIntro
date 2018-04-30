from random import randint, sample, shuffle, choice
from time import sleep

isim = input("yarinizin ismini giriniz: ")
sleep(1)
print("%s için papatya falı başlatılıyor:" % isim)
sleep(1)

yaprak_sayisi = randint(20,30)
son_durum = ''
durumlar = ['seviyor','sevmiyor']

for i in range(0,yaprak_sayisi):
    son_durum = durumlar[i % 2]
    print(son_durum, "iterasyon: ", i, "mod: ", i % 2)
    sleep(.5)

sleep(2)
print("hmmm")
sleep(1)
print("hmmmmmm")
sleep(1)

if son_durum=='sevmiyor':
    print("%s seni sevmiyor!! Ahahahahahha" % isim)
else:
    print("papatya falı işte, çok da şey etme")

