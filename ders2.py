# -*- coding: utf-8 -*-
x = 3
y = 'adnan'

print(x, y)

x == 3 # iki = mantıksal eşitlik demektir

print('x==3', x==3)
print('x>3' , x>3)
print('x>=3' , x>=3)

print(type(x))
print(type(x==3))

print(x is 3)

print(x==4)
print(x!=4)


b = True
print(not b)

print("############")

katil = 'adnan'
print(katil == 'cumali')
print(katil != 'cumali')

print(katil is 'cumali')
print(katil is not 'cumali')


# Olgu: Adnan ve Mümtaz cinayeti beraber işlemiştir.
katil = "Adnan ve Mümtaz"

print('Adnan' in katil)

print('###############')

katil = 'Adnan'
# tahmin = input('tahmininizi giriniz')
tahmin = 'Tuleyman'

soru = 'katil %s. Di mi?' % tahmin
cevap = katil == tahmin
tepki = 'Vatandajj türkçe konuş!'

print(soru)
print(cevap)
print(tepki)

print('###### AND ile OR #######')

katil = 'Adnan'
azmettirici = 'Kazim'

print(katil == 'Adnan' and azmettirici == 'Kazım')
print(katil == 'Adnan' and azmettirici == 'Tülay')
print(katil == 'Tülay' and azmettirici == 'Kazım')
print(katil == 'Tülay' and azmettirici == 'Adnan')


print(katil == 'Adnan' or azmettirici == 'Kazım')
print(katil == 'Adnan' or azmettirici == 'Tülay')
print(katil == 'Tülay' or azmettirici == 'Kazım')
print(katil == 'Tülay' or azmettirici == 'Adnan')

print('##################')

# param = input('Cüzdanınızı girniz: ')
param = '200'
param = int(param)

if param <= 200:
    print('Hediye: Kaşağı')
else:
    print('Hediye: Bak aşkım bugün senin için kendime')


print('##################')

param = input('Cüzdanınızı girniz: ')
if len(param) == 0:e
    param = 100
    print("para girmediniz, default değer 100'dür")
else:
    param = int(param)

if param <= 200:
    print('Hediye: Kaşağı')
elif param <= 1000:
    print('Hediye: Bak aşkım bugün senin için kendime')
else:
    print('Ayy boşver o herifi, bir versacesi bile yoktu')


## Sayı 100 ile 50 arasında mı?

sayi = int(input("sayıyı gir! "))
if sayi > 50 and sayi < 100:
    print("Aradadır")
elif sayi == 50 or sayi == 100:
    print("Tam üstüne bastın, ayağını kaldır")
else:
    print("Ne bileyim nerededir!?!?!")

