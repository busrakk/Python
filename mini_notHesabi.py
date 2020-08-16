
print('*** NOT HESAPLAMA ***')

vize = int(input('Vize notu : '))
final = int(input('Final notu : '))

ort = (vize*0.4) + (final*0.6)

if (ort > 50):
    if(final > 50):
        print(f'Ortalama : {ort}'
              '\nDersi Geçme Durumu : Başarılı')
    else:
        print(f"Ortalama : {ort}"
              "\nDersi Geçme Durumu : Başarısız"
              "\nFinal notu 50'den az")

else:
    print(f"Ortalama : {ort}"
          "\nDersi Geçme Durumu : Başarısız"
          "\nOrtalama 50'den az")


