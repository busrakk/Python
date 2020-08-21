# 2 sayı arasında tüm asalları bula

def asalSayilariBul(sayi1, sayi2):
    #sayi2 de döngüye katmak için +1 
    for sayi in range(sayi1, sayi2+1 ):
        if sayi > 1:
            for i in range(2, sayi):
                if(sayi % i == 0):
                    break
            else:
                    print(sayi)

sayi1 = int(input('1. sayi : '))
sayi2 = int(input('2. sayi : '))

asalSayilariBul(sayi1, sayi2)