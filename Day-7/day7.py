import random

stages = [
    '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
    '''
  +---+
  |   |
  O   |
 /    |
      |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
    '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
# 1. adım: Kelime Seçimi
kelimeler = ["balık", "kuş", "hamsi"]
secilen = random.choice(kelimeler)

# Kelimenin harflerini listeye dönüştürme
display = ["_" for _ in secilen]
uzunluk = len(secilen)
print(display)
numero = 6

while True:
    tahmin = input("Bir harf tahmin et: ").lower()
    if tahmin in display:
        print("Bu harfi zaten tahmin ettiniz.")
        continue

    if tahmin not in secilen:
        numero -= 1
        print(stages[numero])
        if numero == 0:
            print("Kaybettiniz! Doğru kelime '{}' idi.".format(secilen))
            break
    else:
        for position in range(uzunluk):
            letter = secilen[position]
            if letter == tahmin:
                display[position] = letter
                print(stages[numero])
                
        print(display)

    if "_" not in display:
        print("Kazandınız! Kelime: '{}'".format(secilen))
        break




