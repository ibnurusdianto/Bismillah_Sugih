import random 

# contoh random rand range int 
random_number = random.randint(1, 100)
print(random_number)  # Output: a random integer between 1 and 100

# contoh random rand range float
random_float = random.uniform(1.0, 10.0)
print(random_float)  # Output: a random float between 1.0 and 10.0

# memiliki 2 list 5 angka acak
list1 = [random.randint(1, 100) for _ in range(5)]
list2 = [random.randint(1, 100) for _ in range(5)]

# lakukan shuffle pada list1
random.shuffle(list1)
print("List 1:", list1)
print("List 2:", list2)

