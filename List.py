"""
List adalah data struktur yang digunakan untuk menyimapan data, namun list
memiliki kelebihan yaitu bisa duplikasi, bisa diubah, dan bisa diurutkan, serta bisa 
diakses dengan index. List menggunakan tanda kurung siku [] untuk membuat 
"""

# membuat list
family = ["Ayah", "Ibu", "Adik", "Kakak"]
# mengakses list dengan index
print(family[0])  # output: Ayah
print(family[1])  # output: Ibu
print(family[2])  # output: Adik
print(family[3])  # output: Kakak

# menampilkan family 
print(family)  # output: ['Ayah', 'Ibu', 'Adik', 'Kakak'] 

# menampilkan family dengan indexing 
for idx, i in enumerate(family):    
    print(f"{idx},{i}")  # output: 0,Ayah
                                         #         1,Ibu
                                         #         2,Adik
                                         #         3,Kakak
                                         
                                         
# menghapus list dengan del
del family[0]  # menghapus Ayah

# dengan remove
family.remove("Ibu")  # menghapus Ibu 


 