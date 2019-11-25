f = open("test")
print(f)

for line in f:
    print(line)
print()
#print(f.read())
f.close()

try:
    f = open("test")
    #cos tu robimy
except Exception:
    print("Wyjatek")
finally:
    f.close()

#manager kontekstu
with open("test", encoding='utf-8') as f:
    print(f.read())
