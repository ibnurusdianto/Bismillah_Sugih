# user input sederhana
name = input("Masukkan nama Anda: " )
print(f"Hello, {name}! Selamat belajar Python.") 

# user input dengan tipe data 
age = int(input("Masukkan umur Anda: " ))   
print(f"Umur Anda adalah {age} tahun.")

# user input dengan try expect
try:
    number = float(input("Masukkan sebuah angka: " ))
    print(f"Anda memasukkan angka: {number}")
except ValueError:
    print("Input tidak valid. Harap masukkan sebuah angka.")
    

# input dengan validation dan sanitization 
while True:
    email = input("Masukkan alamat email Anda: " )
    if "@" in email and "." in email:
        print(f"Email yang valid: {email}")
        break
    else:
        print("Email tidak valid. Harap masukkan alamat email yang benar.")


# user input dengan expection handling untuk pembagian
try:
    num1 = float(input("Masukkan angka pertama: " ))
    num2 = float(input("Masukkan angka kedua: " ))
    result = num1 / num2
    print(f"Hasil pembagian: {result}")
except ValueError:
    print("Input tidak valid. Harap masukkan angka.")
except ZeroDivisionError:
    print("Error: Pembagian dengan nol tidak diperbolehkan.")
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
    
# Multiline input processing
print("Masukkan beberapa baris teks (ketik 'END' untuk selesai):")
lines = []
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    lines.append(line)
print("Anda memasukkan:")
for idx, line in enumerate(lines, start=1):
    print(f"{idx}: {line}")
    
    
    
    
    
    