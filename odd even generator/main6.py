# while boolean
# output
# operator assignment


# a = int(input("masukan angka pertama"))
# b = int(input("masukan angka kedua"))

# while a <= b:
#     print(a)
#     a = a + 1

# odd even generator

print("mau angka ganjil atau genap")
print("1. ganjil")
print("2. ganap")
a = int(input("mau angka ganjil atau genap"))
b = int(input("mau sampe angka berapa?"))
if a == 1:
    while a <= b:
        print(a)
        a = a + 2
elif a == 2:
    while a <= b:
        print(a)
        a = a + 1