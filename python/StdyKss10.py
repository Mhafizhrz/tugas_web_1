class staticArray :
    def __init__(self,n):
        self.data = [None] * n

    def get_at(self, i):
        if not (0<= 1 < len(self.data)) : raise IndexError
        return self.data [i]

    def set_at(self, i,x):
        if not (0<= 1 < len(self.data)) : raise IndexError
        self.data[i] = x

array1 = staticArray(20)
array2 = staticArray(20)
array3 = staticArray(20)
array4 = staticArray(20)
array5 = staticArray(20)
nakhir = staticArray(20)

# tampilan awal
print("Program data nilai mahasiswa")
print("======================")
n =  int (input ("Jumlah mahasiswa : "))
print()
print("Input nilai mahasiswa ")

# perulangan input
for k in range (n) :
    nama = input("Nama : ")
    array1.set_at(k,(nama))
    harian = int(input("Nilai Harian : "))
    array2.set_at(k,(harian))
    tugas = int(input("Nilai Tugas : "))
    array3.set_at(k,(tugas))
    uts = int(input("Nilai UTS : "))
    array4.set_at(k,(uts))
    uas = int(input("Nilai UAS : "))
    array5.set_at(k,(uas))
    print()

# prooses nilai akhir
for k in range (n):
    nakhir.set_at (k,((0.30 * array2.get_at (k))) + ((0.30 * array3.get_at(k))) + ((0.20 * array4.get_at(k)))+ ((0.20 * array5.get_at(k))))

# tampilan hasil
print("Laporan DAta Nilai Mahasiswa")
print("============================")
print('NO', '','NAMA','\t','HARIAN', '','TUGAS', '\t', 'UTS','\t','UAS','\t','NILAI AKHIR')

for i in range(n) :
    print(i+1,'',array1.get_at(i),'\t',array2.get_at(i),'\t',array3.get_at(i),'\t',array4.get_at(i),'\t',array5.get_at(i),'\t',nakhir.get_at(i), end ='\n')