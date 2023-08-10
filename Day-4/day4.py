# import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random()
# print(random_float)

# random_float = random.random() * 5
# print(random_float)

# #! Lists
# states = ["Delaware", "Pennsylnania", "California", "NewYork"]

# print(states[1])

# # Bu şekilde değiştirilebilir
# states[1] = "Pencilvania"

# print(states)

# # listenin sonuna eleman ekleme sadece 1 tane append()

# states.append("Devrans")
# print(states)

# # birden fazla eleman ekleme extend()

# states.extend(["Zeyneps","Emines"])
# print(states)

# position = "32"

# cols = position[0]
# print(cols)

sayi = int(input("Sayı Gir"))
fax = []
while sayi > 0:
    fax.insert(1, sayi)
    sayi -= 1

def diziyi_carp(dizi):
    carpim = 1
    for eleman in dizi:
        carpim *= eleman
    return carpim

sonuc = diziyi_carp(fax)
print(sonuc)

    
