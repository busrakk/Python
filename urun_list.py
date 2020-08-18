
print(' *** Ürün Listesi Oluşturma ***')
urunler  = []
sayac = 0

adet = int(input('Kaç ürün eklemek istiyorsunuz :'))

while(sayac < adet):
    name = input('ürün ismi : ')
    price = input('ürün fiyatı : ')
    
    #dictionary listesi 
    urunler.append({
        
        'name' : name,
        'price' : price
    })
    
    sayac = sayac + 1

for urun in urunler :
    print(f'ürün adı : {urun["name"]} ürün fiyatı : {urun["price"]}')
          
          
