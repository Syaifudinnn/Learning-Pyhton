#header
print('----------------------------')
print('-- Hitung Rata-Rata Nilai --')
print('----------------------------\n')

#fungsi hitung rata-rata
def hitung_rata_rata(nilai):
    return sum(nilai) / len(nilai)

#list nilai
list_nilai = []

#input nilai
for i in range(5):
    nilai = float(input(f'Masukkan nilai ke-{i+1} : '))
    list_nilai.append(nilai)

#hitung rata-rata dgn memanggil fungsi hitung_rata_rata
rata = hitung_rata_rata(list_nilai)

#kategori nilai
if rata >= 90:
    kategori = 'Sangat Baik'
elif rata >= 80:
    kategori = 'Baik'
elif rata >= 70:
    kategori = 'Cukup'
elif rata >= 60:
    kategori = 'Kurang'
else:
    kategori = 'Sangat Kurang'

#output
print(f'\nRata-rata nilai : {rata}')
print('Kategori : ',kategori)