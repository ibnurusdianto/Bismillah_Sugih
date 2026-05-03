# Otomatis atau implisit konversi tipe data
# integer ke float 
a = 10 
b = 3.14
c = a + b
print(c) # Output: 13.14

# manual - eksplisit konversi tipe data
# string ke integer
x = "100"
y = int(x)
print(y) # Output: 100

# misal boolean tambah integer, boolean true nilai 1, false nilai 0
a = True 
b = 5 
tambah = a + b   
print(tambah)
print(type(tambah)) # Output: 6, <class 'int'> 

# bisa juga konversi antar sistem bilangan komputer 
# desimal ke biner 
a = 35321  
toBiner = bin(a)
print(toBiner) 
toHexa = hex(a)
print(toHexa)
toOctal = oct(a)
print(toOctal)

"""
Lakukan terus untuk semua jenis tipe data yang ada di python 
"""

# bisa juga untuk data struktur seperti list, tuple, set, dict 

# misal set to list 
mySet = {1, 2, 3, 4, 5}
print(type(mySet)) # Output: <class 'set'>
print(mySet) # Output: {1, 2, 3, 4, 5}
myList = list(mySet) 
print(type(myList)) # Output: <class 'list'>
print(myList) # Output: [1, 2, 3, 4, 5]

# jika ke dictioanry harus menambahkan key dan value, jika tidak kita pake dengan cara default yaitu dengan menggunakan index sebagai key dan value sebagai value
myList = ['a', 'b', 'c']
myDict = dict(enumerate(myList))
print(type(myDict)) # Output: <class 'dict'>
print(myDict) # Output: {0: 'a', 1: 'b', 2: 'c'} 

# selain enumarate kita juga bisa menggunakan 
# zip untuk membuat dictionary dari dua list, 
# satu untuk key dan satu untuk value
keys = ['name', 'age', 'city']
values = ['Alice', 30, 'New York']
myDict = dict(zip(keys, values))
print(type(myDict)) # Output: <class 'dict'>
print(myDict) # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# selain zip kita juga bisa menggunakan dict comprehension untuk membuat dictionary dari list
myList = ['a', 'b', 'c']
myDict = {i: myList[i] for i in range(len(myList))}
print(type(myDict)) # Output: <class 'dict'>
print(myDict) # Output: {0: 'a', 1: 'b', 2: 'c'}

# dan masih banyak lagi cara untuk melakukan konversi tipe data di python, tergantung kebutuhan dan konteksnya. 



