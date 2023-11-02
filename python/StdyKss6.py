print("Input Data Gajih")
print('*********************')
print()


nama = input("Masukkan Nama :")
pokok = int(input('Masukkan Gajih Pokok :'))
print()
print("Pilihan Jabatan")
print("Direktur = 1")
print("Manajer = 2")
print("Karyawan = 3")
print()
gol = int(input('Masukkan Jabatan :'))

if gol == 1 :
    a= ('Direktur')
    b= int('3000000')
elif gol == 1 :
    a= ('Manager')
    b= int('2000000')
elif gol == 3 :
    a= ('Karyawan')
    b= int('1000000')

print()
print("Nama Karyawan : ", nama )
print("Gajih Pokok : ", pokok )
print("Jabatan : ", a )
print("Bonus/Tunjangan : ",b  )


pb = int (pokok * 0.05)
pp = int ((pokok + b) * 0.01)
tg = pokok + b - pb - pp

print()
print()

print("Laporan Data Gaji")
print('*********************')
print()

print("Nama Karyawan : ", nama )
print("Gajih Pokok : ", pokok )
print("Bonus/Tunjangan : ", b )
print("Potongan BPJS : ", pb )
print("Potongan Pajak : ", pp )
print("Terima Gajih : ", tg )