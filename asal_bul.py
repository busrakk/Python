#Fonksiyon kısmı
def asal_bul(sayi):
    
    if sayi == 1:
        return False
    
    elif sayi == 2:
        return True
    
    else:
        #2 den girilen sayiya kadar..
        for i in range(2 , sayi):
            if sayi % i == 0:
                return False
        return True

#Döngü doğru olduğu sürece devam eder    
while True:
    sayi = int(input("Bir Sayı Giriniz : "))
    
    if asal_bul(sayi):
        print(sayi, "Asal Sayıdır.")
        
    else:
        print(sayi, "Asal Sayı Değildir.")

        
        
