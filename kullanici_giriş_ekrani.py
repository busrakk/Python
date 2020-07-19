print("--------KULLANICI GİRİŞ EKRANI--------")

#sistemde kayıtlı bilgiler
adi_kullanici = "busra"
parola = "123456"

#sistemdeki kayıtlı bilgilerin uzunluğu
uzunluk_ad = len(adi_kullanici)
uzunluk_p = len(parola)

#sisteme girilen bilgiler
print("Sisteme Giriş Yapabilmeniz için Kullanıcı Adınızı ve Parolanızı Giriniz.")
g_adi_kullanici = input("Kullanıcı Adı : ")
g_parola = input("Parola : ")

#girilen bilgilerin uzunluğu
uzunluk_ad_g = len(g_adi_kullanici)
uzunluk_p_g = len(g_parola)

#bilgi kontrol 
if adi_kullanici != g_adi_kullanici and parola == g_parola:
    print("Kullanıcı Adınızı Yanlış Girdiniz.")
    
    if uzunluk_ad > uzunluk_ad_g:
        print("Girdiğiniz Kullanıcı Adı Kısa")
        
    else:
        print("Girdiğiniz Kullanıcı Adı Uzun")
        
    print("Girmeniz gereken kullanıcı adı {} karakterden oluşmaktadır.".format(uzunluk_ad))
    print("Tekrar Deneyiniz..")
    
    
elif adi_kullanici == g_adi_kullanici and parola != g_parola:
    print("Parolanızı Yanlış Girdiniz.")
    
    if uzunluk_p > uzunluk_p_g:
        print("Girdiğiniz Parola Kısa")
        
    else:
        print("Girdiğiniz Parola Uzun")
        
    print("Girmeniz gereken parola {} karakterden oluşmaktadır.".format(uzunluk_p))
    print("Tekrar Deneyiniz..")  
    
    
elif adi_kullanici != g_adi_kullanici and parola != g_parola:
    print("Kullanıcı Adınızı ve Parolanızı Yanlış Girdiniz.")
    
    if uzunluk_ad > uzunluk_ad_g and uzunluk_p > uzunluk_p_g:
        print("Girdiğiniz Kullanıcı Adı ve Parola Kısa")
        
    elif uzunluk_ad > uzunluk_ad_g and uzunluk_p < uzunluk_p_g:
        print("Girdiğiniz Kullanıcı Adı Kısa ve Parola Uzun")
        
    elif uzunluk_ad < uzunluk_ad_g and uzunluk_p > uzunluk_p_g:
        print("Girdiğiniz Kullanıcı Adı Uzun ve Parola Kısa")
        
    else:
        print("Girdiğiniz Kullanıcı Adı ve Parola Uzun") 
        
    print("Girmeniz gereken kullanıcı adı {} ve parola {} karakterden oluşmaktadır.".format(uzunluk_ad, uzunluk_p))
    print("Tekrar Deneyiniz..")   
    
    
else:
    print("Sisteme Başarıyla Giriş Yaptınız.")
    
    
    