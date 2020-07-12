list = [ "a", "b","c", "d" ]

#eğer atama yapmak istersek
list[1]= "e"
list


#birden fazla elemana atama yapmak istersek
list[0:3]= "k","l","m"
list

 

#listeye yeni eleman eklemek istersek
list + ["i"]



#kalıcı olarak eklemek istersek atama yapmamız gerekir
list = list +["i"]
list


#listeden eleman silmek istersek
del list[2]
list

#LISTE METODLARI

#listeye eklemek istersek
list.append("p")
list


#listeden çıkartmak istersek
list.remove("p")
list


#indekslerle eleman eklemek istersek
list.insert(0,"python")
list


#indekslerle liste sonuna eleman eklemek istersek
list.insert(len(list), "program")
list


#indekslerle eleman silmek istersek
list.pop(4)
list

"""
--------------------

"""
new_list=[1,9,9,2,5]

#listedeki belirli elemanın kaç tane olduğunu öğrenmek istersek
new_list.count(9)


#kopyalamak için
temp_list = new_list.copy()
temp_list


#2 listeyi birleştirmek istersek
new_list.extend(["ayse",10])
new_list


#elemanın hangi indekste olduğunu öğrenmek istersek
new_list.index("ayse")


#liste elemanlarını ters çevirmek istersek
new_list.reverse()
new_list


#sıralama yapmak istersek
list=[9,1,7,5]
list.sort()
list


#liste içini temizlemek istersek
list.clear()
list




