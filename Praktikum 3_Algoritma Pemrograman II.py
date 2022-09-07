def nambah(angka1,angka2):
    hasil1 = angka1 + angka2
    return hasil1
def kurang(angka1,angka2):
    hasil2 = angka1 - angka2
    return hasil2
def kali(angka1,angka2):
    hasil3 = angka1 * angka2
    return hasil3
def bagi(angka1,angka2):
    hasil4 = angka1 / angka2
    return hasil4

while True:
    try:
        angka1 = float(input("Masukkan angka 1 : "))
        angka2 = float(input("Masukkan angka 2 : "))
    except ValueError:
        print("Error")
        continue
    tanda = input("Operasi apa ? ")
    if tanda == "+":
        print(nambah(angka1,angka2))
    elif tanda == "-":
        print(kurang(angka1,angka2))
    elif tanda == "*":
        print(kali(angka1,angka2))
    elif tanda == "/":
        print(bagi(angka1,angka2))
    else:
        print("Error")
        continue
    break