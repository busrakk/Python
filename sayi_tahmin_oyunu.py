#random sayı üretme
import random
sayi = random.randint(1,100)

print("""***************************
TAHMİN OYUNUNA HOŞGELDİNİZ
***************************""")

print("""\nOyun Kuralları :\n 
1- Tahmin Edilecek Sayi 1-100 arasında.
2- 5 Tahmin Hakkınız Var.
Kolay Gelsin :) """)

#5 tekrar
for i in range(5):
    tahmin = int(input("Tahminini Gir : "))
    
    if tahmin < sayi and i<4:
        print("Bilemedin.. Biraz yukarı tahmin et..")
        
    elif tahmin > sayi and i<4:
        print("Bilemedin.. Biraz aşağı tamin et.. ")
        
    elif i==4 and tahmin != sayi:
        print("5 Kez Yanlış Tahmin Yaptınız..")
        print("** Bilgisayarın Tuttuğu Sayi {} **\n".format(sayi))
    
    else:
        print("Tebrikler.. Bildin\n")
        break
        
print("OYUN BİTTİ..") 
       
