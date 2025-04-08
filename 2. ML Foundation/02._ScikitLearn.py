#program prediksi produktivitas berdasarkan jam tidur

from sklearn.linear_model import LinearRegression
import numpy as np

#data : jam tidur dan produktivitas
jam_tidur = np.array([[5], [6], [7], [8], [9]])
produktivitas = np.array([60, 70, 80, 90, 100])

#membuat dan melatih model
model = LinearRegression()
model.fit(jam_tidur, produktivitas)

#prediksi produktivitas
prediksi = model.predict([[6], [5], [24]])
print("Prediksi produktivitas untuk 6 jam tidur :", prediksi[0])
print("Prediksi produktivitas untuk 5 jam tidur :", prediksi[1])
print("Prediksi produktivitas untuk 9 jam tidur :", prediksi[2])