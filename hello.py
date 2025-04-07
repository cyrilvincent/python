import sys

print("Hello world")
print("toto")
print(sys.version)

a = 1
b = a + 2
c = b // 2
print(a, b, c)
print(3 % 2)

a = a + 1
print(a)
a += 1
print(a)
a *= 2
print(a)

print("j'aime")
print('j\'aime\"\\\t\ntoto')
print("""Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability 
with the use of significant indentation.[33]
Python is dynamically type-checked and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.
Python（英式發音：/ˈpaɪθən/；美式發音：/ˈpaɪθɑːn/），是一種廣泛使用的直譯式、進階和通用的程式語言。Python支援多種程式設計範式，包括結構化、程序式、反射式、物件導向和函數式程式設計。它擁有動態型別系統和垃圾回收功能，能夠自動管理主記憶體使用，並且其本身擁有一個巨大而廣泛的標準庫。它的語言結構以及物件導向的方法，旨在幫助程式設計師為小型的和大型的專案編寫邏輯清晰的程式碼。
""")

captain_age = 33
print(captain_age)
toto = "33"
# print(captain_age + toto)
print(type(toto))

captain_age = input("Saisir l'age du capitaine: ")
captain_age = int(captain_age)
print(captain_age + 1)

print("L'age du capitaine est : " + str(captain_age))
print(f"L'age du capî\u03A3taine est : {captain_age / 2:.2f}")

