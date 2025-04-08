#visualisasi performa mahasiswa

import matplotlib.pyplot as plt
import seaborn as sns

#data
nilai = [80, 90, 75, 60, 85]
nama = ['Andi', 'Budi', 'Cindy', 'Doni', 'Eka']

#klasifikasi kelulusan
status = ['Lulus' if n >= 75 else 'Tidak Lulus' for n in nilai]

#hitung lulus dan tidak
lulus_count = status.count('Lulus')
tidak_lulus_count = status.count('Tidak Lulus')

#plot bar
plt.bar(nama, nilai, color='skyblue')
plt.title('Grafik Mahasiswa')
plt.xlabel('Nama Mahasiswa')
plt.ylabel('Nilai')
plt.show()

#pie chart
plt.figure(figsize=(6, 6))
plt.pie([lulus_count, tidak_lulus_count], 
         labels=['Lulus', 'Tidak Lulus'], 
         autopct='%1.1f%%',
         colors=['green', 'red'], 
         startangle=140)
plt.title('Persentase Kelulusan')
plt.show()

#implementasi seaborn
plt.figure(figsize=(6, 4))
sns.boxplot(data=nilai, color='skyblue')
plt.title('Grafik Mahasiswa dengan Seaborn')
plt.xlabel('Nilai')
plt.show()