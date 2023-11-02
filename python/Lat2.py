jawab = 'Ya'
hitung = 0

while(True):
    hitung += 1
    jawab = input("Ulang lagi tidak? ")
    if  jawab == 'Tidak':
        break

print("")
print(f" Total perulagan: {hitung}")
print("")