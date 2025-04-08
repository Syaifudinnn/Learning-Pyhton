import numpy as np
import pandas as pd

#numpy
nilai = np.array([80, 90 ,95, 70, 83])

print("Rata-rata nilai : ", np.mean(nilai))
print("Nilai tertinggi : ", np.max(nilai))

#pandas
data = {
    'Nama' : ['Andi', 'Budi', 'Cindy', 'Doni'],
    'Umur' : [20, 21, 19, 22],
    'Nilai' : [80, 90, 95, 70]
}

#buat dataframe
df = pd.DataFrame(data)

#tambah kolom status
df['status'] = df['Nilai'].apply(lambda x: 'Lulus' if x >= 75 else 'Tidak Lulus')

#tampilkan dataframe lengkap
print('\n', df)

#statistik nilai
print("\nRata-rata nilai : ", df['Nilai'].mean())
print("Nilai tertinggi : ", df['Nilai'].max())

#jumlah lulus dan tidak
jumlah_status = df['status'].value_counts()
print("\nJumlah Lulus : ", jumlah_status['Lulus'])
print("Jumlah Tidak Lulus : ", jumlah_status['Tidak Lulus'])