print("Input Data Barang")
print('-----------------')
print()

while(True):
    jawab = 'Ya'
    namabr = input("Masukkan Nama Barang :")
    sawal = int(input('Masukkan Saldo Awal :'))
    bamas = int(input('Masukkan Barang Masuk :'))
    balur = int(input('Masukkan Barang Keluar :'))

    print()
    print("Pilihan :")
    print("Ya & Tidak")
    print()
    jawab = input("Apakah Anda Ingin Menginput Lagi? ")
    print()

    if  jawab == 'Tidak':
        break

print()
print("Nama Barang : ", namabr )
print("Saldo Awal : ", sawal )
print("Barang Masuk : ", bamas )
print("Barang Keluar : ", balur )

print()
print("Laporan Data Barang")
print('-------------------')
print()

print("| Nama Barang | Saldo Awal | Brg Masuk | Brg Keluar | Saldo Akhir | Keterangan|")
print('------------------------------------------------------------------------------')
sa = int (sawal + bamas - balur)

if sa <= 3 :
    a= ('Habis')
elif sa <= 16 :
    a= ('Hampir Habis')
elif sa >= 17 :
    a= ('Tersedia')

print (('      '),namabr,('        '),sawal,('         '),bamas,('        '),balur,('      '),sa,('        '),a,('  '))