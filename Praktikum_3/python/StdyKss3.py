print("Input Profile dan Nilai Akhir")
print('-----------------------------')
print()

namamhs = input("Masukkan Nama  :")
npm = input("Masukkan NPM :")
niha = int(input('Masukkan Nilai Harian :'))
nitu = int(input('Masukkan Nilai Tugas :'))
niut = int(input('Masukkan Nilai UTS :'))
niua = int(input('Masukkan Nilai UAS :'))
print()

print("Data Nilai Akhir")
print('----------------')


print("Nilai Harian : ", niha )
print("Nilai Tugas : ", nitu )
print("Nilai UTS : ", niut )
print("Nilai UAS : ", niua )
print()


print("Hasil Nilai Akhir")
print('-----------------')
print()

nh = int (niha * 0.30)
nt = int (nitu * 0.30)
nut = int (niut * 0.20)
nua = int (niua * 0.20)
na = int (nh+nt+nut+nua)

print("Nama  : ", namamhs )
print("NPM : ", npm )
print("Nilai Harian : ", nh )
print("Nilai Tugas : ", nt )
print("Nilai UTS : ", nut )
print("Nilai UAS : ", nua )
print("Nilai Akhir : ", na )