l = ["python","programlama"]
s = set(l)
s

#eleman ekleme
s.add("ile")
s


#eleman silme
s.remove("ile")
s

#-----------------------

set1 = set([1,3,5])
set2 = set([1,2,3])

#iki kümenin farkı
set1.difference(set2)
set1 - set2

set2.difference(set1)
set2 - set1


#ikisine aynı anda bakma
set1.symmetric_difference(set2)


#kesişim 
set1.intersection(set2)
set1 & set2


#birleşim
set1.union(set2)


#kaydetme
set1.intersection_update(set2)
set1


#-------------------------

set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])

# 2 kümenin kesisimini sorgulama
set1.isdisjoint(set2)


#bir kümenin elemanları başka kümede olup olmadığı
#alt kümesi 
set1.issubset(set2)


#kümenin kapsayıp kapsamadığı
set2.issuperset(set1)


