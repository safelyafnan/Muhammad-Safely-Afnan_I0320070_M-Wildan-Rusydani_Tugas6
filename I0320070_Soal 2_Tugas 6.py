nilai = []
banyak_nilai = int(input('Berapa banyak nilai yang ingin dihitung: '))
for i in range(banyak_nilai):
    nilainya = int(input('masukkan nilai ke-{} : '.format(i+1)))
    nilai.append(nilainya)
print('hasil rata-rata adalah : {} '.format(sum(nilai)/banyak_nilai))