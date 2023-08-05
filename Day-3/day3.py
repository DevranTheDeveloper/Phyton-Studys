#! if-elif-else (js le neredeyse aynı)

print("Rollercoster a hoş geldin dostum")
heigth = int(input("Boyunu yaz hele bakim: "))

if heigth >= 120:
    print("Geç bakalım boyun yetiyor")
    age = int(input("Yaşın kaç bakem: "))
    if age <= 12:
        bill = 5
        print("Çocuk tarifesi 5$")
    elif age <= 18:
        bill = 7
        print("Genç tarifesi 7$")
    else:
        bill = 12
        print("Yetişkin tarifesi 12$")
    
    foto = input("Foto isteyen? (E or H)")
    if foto == "E":
        bill += 3
        print(f"Al sana foto da verem borcun: {bill}$")
    elif foto == "H":
        print(f"Fotosuz ücretiniz: {bill}$")
else:   
    print("Olmaz böyle uza da gel")
    
