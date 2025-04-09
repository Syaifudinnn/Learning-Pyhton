#prediksi status lulus berdasarkan nilai dan kehadiran

from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
import pandas as pd

#data
data = pd.DataFrame({
    'Nilai': [80, 60, 95, 50, 75, 40, 85, 55, 90, 65],
    'Kehadiran': [90, 70, 95, 60, 80, 50, 85, 65, 100, 75],
    'Tugas': [85, 65, 90, 55, 80, 45, 88, 60, 92, 70],
    'Lulus': ['Ya', 'Tidak', 'Ya', 'Tidak', 'Ya', 'Tidak', 'Ya', 'Tidak', 'Ya', 'Tidak']
})

#encoding label
data['Lulus'] = data['Lulus'].map({'Ya': 1, 'Tidak': 0})

#buat dan latih mdoel
X = data[['Nilai', 'Kehadiran', 'Tugas']]
y = data['Lulus']
model = DecisionTreeClassifier()
model.fit(X, y)

#evaluasi akurasi model
akurasi = model.score(X, y)
print(f'Akurasi model : {akurasi * 100:.2f}%')

#input nilai dan kehadiran
nilai = int(input("Masukkan nilai : "))
kehadiran = int(input("Masukkan kehadiran : "))
tugas = int(input("Masukkan nilai tugas : "))

#prediksi
input_data = pd.DataFrame([[nilai, kehadiran, tugas]], columns=['Nilai', 'Kehadiran', 'Tugas'])
hasil = model.predict(input_data)

print(f"Prediksi untuk nilai {nilai}, kehadiran {kehadiran}, dan tugas {tugas} :", "Lulus" if hasil[0] == 1 else "Tidak Lulus")

#visualisasi decision tree
plt.figure(figsize=(10, 6))
plot_tree(model,
          feature_names=['Nilai', 'Kehadiran', 'Tugas'],
          class_names=['Tidak Lulus', 'Lulus'],
          filled=True,
          rounded=True,
          fontsize=12)
plt.title('Visualisasi Decision Tree')
plt.show()