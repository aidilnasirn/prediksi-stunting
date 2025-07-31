import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Contoh data prediksi dan label sebenarnya
y_true = ['Stunting', 'Tidak Stunting', 'Stunting', 'Tidak Stunting', 'Stunting', 'Stunting', 'Tidak Stunting', 'Tidak Stunting', 'Stunting', 'Tidak Stunting', 'Stunting', 'Tidak Stunting']
y_pred = ['Stunting', 'Tidak Stunting', 'Stunting', 'Stunting', 'Stunting', 'Tidak Stunting', 'Tidak Stunting', 'Tidak Stunting', 'Stunting', 'Tidak Stunting', 'Stunting', 'Stunting']

# Menghitung confusion matrix
cm = confusion_matrix(y_true, y_pred, labels=['Stunting', 'Tidak Stunting'])

# Membuat visualisasi confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Stunting', 'Tidak Stunting'], yticklabels=['Stunting', 'Tidak Stunting'])
plt.ylabel('Label Sebenarnya')
plt.xlabel('Label Prediksi')
plt.title('Confusion Matrix - Algoritma SVM')
plt.show()