# Konu 1 : Sayılar
x = 3
y = 2


print('Hesaplanan sayı: ', x *y)


## Aritmetik işlemler
print('3 + 2 = ', 3 + 2)
print('3 - 2 = ', 3 - 2)
print('3 * 2 = ', 3 * 2)
print('3 / 2 = ', 3 / 2)
print('3 ** 2 = ', 3 ** 2)

print('6-4-1 = ', 6-4-1)
print('6+4*2 = ', 6+4*2)
print('(6+4)*2 = ', (6+4)*2)


# Metinsel değişkenler
adam = 'adnan'
print(adam)

sayi1 = '1837'
sayi2 = '837'
print(sayi1 + ' ' + sayi2)
print(sayi1, sayi2)
sayi3 = sayi1+sayi2
print(sayi3)

print(sayi1[1])

print('suleym' + 'a'*10 + 'n')
print('hamz' + 'a' * 20)

taslak = 'telefon numaram: '
print(taslak + '05333624888')

taslak = 'telefon numaram %s'
telefon = '05333624888'

print(taslak % telefon)

taslak2 = 'ara beni, %s \n:)))) '
sonuc = taslak2 % '05333624888'
print(sonuc)

print('################\n')
taslak3 =  'ara beni, %s \n:))))\n%s '
telefon = '05333624888'
tarih   = 'akşam 9'

print(taslak3 % (telefon, tarih) )

print('################\n')
s1 = '1837'
print('s1 = ', s1)
s2 = '837'
print('s2 = ', s2)
print(float(s1) + float(s2))


print('################\n')
boy = 178
kilo = 61


# integer ile
boy  = 176
kilo = 60
taslak = 'boyum %i, %i kiloyum, bekarım'
print(taslak % (boy,kilo) )

# float ile
boy  = 178
kilo = 90
taslak = 'boyum %i, %i kiloyum, bekarım \n ayrıca vücut kitle endeksim %f'
vke    = kilo ** 2 / boy
print(taslak % (boy,kilo,vke) )

print('################\n')
kilo = int(input('kilonuzu giriniz: '))
boy  = int(input('boyunuzu giriniz: '))
vke  = kilo ** 2 / boy 
taslak = 'boy %i ve kilo %i için vücut kitle endeksi %f olarak hesaplanmıştır'

print(taslak % (boy,kilo,vke) )




