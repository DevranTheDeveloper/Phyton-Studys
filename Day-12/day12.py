a = 12 #Global Scobe

def new_a():
    a = 10 #Local Scobe
    print(a)
new_a()
print(a)


level = 3
dusman = ["Ayı", "1000 Satır Tayfa", "Ejderha"]

if level < 5:
    new_dusman = dusman[1] #Global Scobe
    
print(new_dusman)

