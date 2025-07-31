import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# Data confusion matrix
confusion_mat = np.array([[498, 140],
                           [91, 571]])

# Membuat heatmap dengan seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_mat, annot=True, fmt='d', cmap='Blues', xticklabels=['Predicted 0', 'Predicted 1'], yticklabels=['Actual 0', 'Actual 1'])

# Menambahkan judul dan label
plt.title('Confusion Matrix - Algoritma SVM')
plt.xlabel('Predicted')
plt.ylabel('Actual')

# Menampilkan plot
plt.show()