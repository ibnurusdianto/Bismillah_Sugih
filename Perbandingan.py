a = 10 
b = "10"

print(a == b) # Output: False
print(a != b) # Output: True
print(a > int(b))  # Output: False
print(a < int(b))  # Output: False
print(a >= int(b)) # Output: True
print(a <= int(b)) # Output: True
# Perbandingan antara dua string

str1 = "Hello"
str2 = "World"

print(str1 == str2) # Output: False
print(str1 != str2) # Output: True
print(str1 > str2)  # Output: False (karena "H" < "W")
print(str1 < str2)  # Output: True
print(str1 >= str2) # Output: False
print(str1 <= str2) # Output: True


# perbanding antara dua list
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2) # Output: True (karena isi list sama)
print(list1 != list2) # Output: False
print(list1 > list2)  # Output: False (karena isi list sama)
print(list1 < list2)  # Output: False (karena isi list sama)
print(list1 >= list2) # Output: True
print(list1 <= list2) # Output: True
