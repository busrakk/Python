#sürekli döngü
while True :
    
    parola = input("Bir Parola Belirleyin: ")
    
    #döngünün  etmesi için continue ..
    if not parola:
        print("Parola Kısmı Boş Geçilmez !!")
        continue
    
    elif len(parola)<8:
        print("Parola 8 Karakterden Az Olmamalı !!")
    
    #döngü sonlanması için break kullan..    
    else:
        print("Parolanız Başarıyla Oluşturulmuştur.")
        break


