
print(' Girilen Sayıları Sıralama ')

sayi1 = int(input('1. Sayıyı gir : '))
sayi2 = int(input('2. Sayıyı gir : '))
sayi3 = int(input('3. Sayıyı gir : '))

if (sayi1 > sayi2) and (sayi1 > sayi3):
    if(sayi2 > sayi3):
        print(f'sıralama : {sayi1} > {sayi2} > {sayi3}')
    else:
        print(f'sıralama : {sayi1} > {sayi3} > {sayi2}')
  
elif(sayi2 > sayi1) and (sayi2 > sayi3):
    if(sayi1 > sayi3):
        print(f'sıralama : {sayi2} > {sayi1} > {sayi3}')
    else:
        print(f'sıralama : {sayi2} > {sayi3} > {sayi1}') 
        
else:
    if(sayi1 > sayi2):
        print(f'sıralama : {sayi3} > {sayi1} > {sayi2}')
    else:
        print(f'sıralama : {sayi3} > {sayi2} > {sayi1}')        
      
