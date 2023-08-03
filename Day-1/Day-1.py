# print, input, variables, manipulations, basic math...

# ! print() kullanırken boşluklara ve syntax hatalarına dikkat edilmelidir

print("Hello World!")

#* print() ile satırları ayırmak için "\n" kullanrırız

print("Devran\nSever")

# ! input() temelle printle aynıdır ama bu sefer veri göndermez veri alır 

input("Adınız nedir? ")

#* bunu yazdırmak için print kullanalım

print("Adınız: " +input("Adınız nedir? "))

# * bunu değişken (variable) kullanarak daha kısa yapabiliriz

x = input("Adınız Nedir? ")
print(x)

# ! manipulations kullanmak sayısal işlemlerde önemlidir çünkü bir değer yazdıracaksak bunun sadece string veya sadece intager olması gerekmektedir bunun için de: str() ve int() taglerini kullanırız

x = 12 
y = "Merhaba"

# print(x + y) #! yanlış kullanım
print(str(x) + y) #* doğru kullanım

#! toplama çıkama gibi işlemleri kullanırken string ifadeleri intager ifadelere dönüştürebiliriz

x = 12 
y = "23"

print(x + int(y)) # gibi

#! eval() ifadesi ile de string ifade içeriside kalmış işlemler yapılabiril 

z = "8 + 3"

print(eval(z)) # bu şekilde kullanılır

# ! int() ifadesini sayıların küsürhatlarını da atmak için kullanabiliriz 

x = 12.5 

print(int(x))

#! karakter uzunluğunu ölçerken len() tagi kullanılır

name = input("Enter your name here ==> ")
length = len(name)

print("Your names length is: " + str(length))