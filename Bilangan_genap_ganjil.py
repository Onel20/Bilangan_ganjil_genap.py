num = int(input("masukkan angka "))

while num%2 == 0 or num < 20 :
    print("Salah!")
    num = int(input("Masukkan angka : "))
else:
    print("True")