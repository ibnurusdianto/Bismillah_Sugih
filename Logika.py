# logika Operasi Logika 

"""
and, true jika kedua true 
or, true jika salah satu true atau keduanya true
not, true jika false, false jika true
"""

# kumpulan semua true dan false 
for x in [True, False]:
    for y in [True, False]:
        print(f"{x} and {y} = {x and y}")
        print(f"{x} or {y} = {x or y}")
        print(f"not {x} = {not x}")
        print(f"not {y} = {not y}")
        print()
