#analisis dataset iris

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import seaborn as sns

#read dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

#pisah fitur dan label
X = df.drop("species", axis=1)
y = df["species"]

#split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#buat dan latih model KNN
knn_model = KNeighborsClassifier()
knn_model.fit(X_train, y_train)

#buat dan latih model decision tree
dt_model = DecisionTreeClassifier()
dt_model.fit(X_train, y_train)

#prediksi KNN
prediksi_knn = knn_model.predict(X_test)
print('Akurasi KNN :', accuracy_score(y_test, prediksi_knn))

#prediksi decision tree
prediksi_dt = dt_model.predict(X_test)
print('Akurasi Decision Tree :', accuracy_score(y_test, prediksi_dt))

#visualisasi scatter
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='petal_length', y='petal_width', hue='species', palette='viridis', s=100)
plt.title('Scatter Plot: Petal Length vs Petal Width')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.grid(True)
plt.show()