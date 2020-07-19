print("**\n\n Kişi Tanıtma Programı ***\n\n HOŞGELDİNİZ.....")

ad = input("Adınızı Giriniz : ")
soyad = input("Soyadınızı Giriniz : ")
dogum_yil = int(input("Doğum Yılınızı Giriniz : "))
dogum_yeri = input("Doğum Yeriniz : ")
okul_no = input("Okul Numaranızı Giriniz : ")
okul = input("Okulunuz : ")
bolum = input("Bölümünüz : ")
sinif = input("Kaçıncı Sınıfsınız : ")

print("{} {} , {} yılında {} ilinde dogmustur.".format(ad, soyad,dogum_yil,dogum_yeri))
print("{} numaralı {} , {} bölümü {}. sınıf öğrencisidir.".format(okul_no,okul,bolum,sinif))
