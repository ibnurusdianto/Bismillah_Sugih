# integer
number = 10 
# float
number = 10.43 
# string
nama = "John Doe"
# boolean
is_active = True
is_deactive = False
# biner 
biner = 0b1010
# octal
octal = 0o12
# hexadecimal
hexadecimal = 0x1A
# complex number
complex_number = 2 + 3j

print("Integer:", number)
print("Float:", number)
print("String:", nama)
print("Boolean Active:", is_active)
print("Boolean Deactive:", is_deactive)
print("Biner:", biner)
print("Octal:", octal)
print("Hexadecimal:", hexadecimal)
print("Complex Number:", complex_number)

"""
Biner, octal, hexa akan otomatis konversi ke integer, karena sistem 
membaca sebagai integer 
"""

# type() untuk mengetahui tipe data
print("Tipe data number:", type(number))
print("Tipe data nama:", type(nama))
print("Tipe data is_active:", type(is_active))
print("Tipe data biner:", type(biner))
print("Tipe data octal:", type(octal))
print("Tipe data hexadecimal:", type(hexadecimal))
print("Tipe data complex_number:", type(complex_number))
