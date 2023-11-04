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
total = staticArray(20)

# tampilan awal
print("Program Data Angkutan Kota")
print("==========================")
print()
n =  int (input ("Jumlah Angkot : "))

# perulangan input
print()
print("Input Data Angkot ")
print()
for k in range (n) :
    nAngkot = input("Nomor Angkot: ")
    array1.set_at(k,(nAngkot))
    tujuan = input("Tujuan : ")
    array2.set_at(k,(tujuan))
    jPenumpang = int(input("Jumlah Penumpang : "))
    array3.set_at(k,(jPenumpang))
    status = input("Status : ")
    array4.set_at(k,(status))
    print()

# tampilan hasil
print("Laporan Data Angkutan Kota")
print("==========================")
print('No', '','Nomor_Angkot', '\t','Tujuan','\t','Jumlah_Penumpang', '\t','Status')

for i in range(n) :
    print(i+1,'',array1.get_at(i),'\t',array2.get_at(i),'\t',array3.get_at(i),'\t',array4.get_at(i), end ='\n')
