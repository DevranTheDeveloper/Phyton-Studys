# number = int(input("Bir sayı gir: "))

        
# def asal_Sayi(number):
#     asal = True
#     for i in range(2, number):
#         if number % i == 0:
#             asal = False
#     if asal == True:
#         print("Bu bir asal sayıdır")
#     else:
#         print("Bu bir asal sayı değildir")
# asal_Sayi(number=number) 

alphabet = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'h', 'i', 'ı', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'q', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'w', 'x', 'y', 'z', ' ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '?', '.', ',', ':', ';']

yonlendir = input("Gizlemek için 'encode' yazınız, ortaya çıkarmak için 'decode' yazınız:\n")

if yonlendir == "encode":
    text = input("Yazınızı giriniz:\n ").lower()
    shift = int(input("Kaydırmak istediğiniz uzunluğu seçin:\n "))
    def encrypt(plain_text, shift_amount):
        chiper_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            chiper_text += new_letter
        print(f"Şifrelenmiş yazınız: {chiper_text}")
    encrypt(plain_text=text, shift_amount=shift)
elif yonlendir == "decode":
    text = input("Şifreli yazıyı giriniz:\n ").lower()
    shift = int(input("Kaydırma sayısını giriniz:\n "))
    def decrypt(encoded_text, shift_decode):
        decoded_text = ""
        for letter in encoded_text:
            position = alphabet.index(letter)
            last_position = position - shift_decode
            last_letter = alphabet[last_position]
            decoded_text += last_letter
        print(decoded_text)
    decrypt(encoded_text=text, shift_decode=shift)
        
