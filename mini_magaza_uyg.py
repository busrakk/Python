print("MAGAZA UYGULAMAMIZA HOŞGELDİNİZ .. \n")

magaza_adi = input("Magaza Adinizi Girin : ")
gelir = int(input("Gelirinizi Girin : "))
sinir = int(input("Sinirinizi Girin : "))

if gelir > sinir:
    print("TEBRİKLER ! " + magaza_adi  + " mağazasından promosyon kazandiniz..")
elif gelir < sinir:
    print("UYARİ ! " + str(gelir) + " cok dusuk gelir..")
else:
    print("Takibe Devam..")
    
print("\nTEKRAR BEKLERİZ...")    
   
    
     
