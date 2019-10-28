s="Hello!"
print(s[0:5]) #od indeksu 0 do 4 wlacznie
print(s[-3]) #3-eci znak od konca

s = "Ruda tańczy jak szalona"
arr = s.split(" ")
print(arr)
print(arr[0])

print(s[0:16:2]) #z indeksu od 0 do 16 ale co drugi znak
print(s[::3]) #caly string co 3-ci znak

#reverse w Pythonie
print(s[::-1])

print("zajecia dzis sie nie odbędą")

print("hello"+"world")
a="Hello"
b="ALX"
print(f"{a}{b}")
print(f"{a} {b}")

x=input("Podaj wartość x")
x=int(x)
print(x,type(x)) #jesli jest input to zawsze zwraca "string"








