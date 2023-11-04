print("Input Data Gajih")
print('*********************')
print()

nama = input("Masukkan Nama :")
pokok = int(input('Masukkan Gajih Pokok :'))
bonus = int(input('Masukkan Bonus/Tunjangan :'))

print()
print("Nama Karyawan : ", nama )
print("Gajih Pokok : ", pokok )
print("Bonus/Tunjangan : ", bonus )

pb = int (pokok * 0.05)
pp = int ((pokok + bonus) * 0.01)
tg = pokok + bonus - pb - pp

print()
print()

print("Laporan Data Gaji")
print('*********************')
print()

print("Nama Karyawan : ", nama )
print("Gajih Pokok : ", pokok )
print("Bonus/Tunjangan : ", bonus )
print("Potongan BPJS : ", pb )
print("Potongan Pajak : ", pp )
print("Terima Gajih : ", tg )
