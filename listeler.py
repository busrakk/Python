list = [ "a", "b","c", "d" ]

#eğer ataması yapma
list[1]= "e"
list


#birden fazla elemana atama yapma
list[0:3]= "k","l","m"
list

 

#listeye yeni eleman ekleme
list + ["i"]



#kalıcı olarak eleman eklemede atama yapmamız gerekir
list = list +["i"]
list


#listeden eleman silme
del list[2]
list

#LISTE METODLARI

#listeye ekleme
list.append("p")
list


#listeden çıkartma
list.remove("p")
list


#indekslerle eleman ekleme
list.insert(0,"python")
list


#indekslerle liste sonuna eleman ekleme
list.insert(len(list), "program")
list


#indekslerle eleman silme
list.pop(4)
list

"""
--------------------

"""
new_list=[1,9,9,2,5]

#listedeki belirli bir elemandan kaç tane olduğunu öğrenme
new_list.count(9)


#kopyalama
temp_list = new_list.copy()
temp_list


#2 listeyi birleştirme
new_list.extend(["ayse",10])
new_list


#elemanın hangi indekste olduğunu öğrenme
new_list.index("ayse")


#liste elemanlarını ters çevirme
new_list.reverse()
new_list


#sıralama yapma
list=[9,1,7,5]
list.sort()
list


#liste içini temizleme
list.clear()
list




