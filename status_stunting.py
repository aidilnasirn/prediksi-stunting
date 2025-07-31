import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# === Data langsung dimasukkan ke DataFrame ===
data = {
    "Status": ["Stunting", "Non-Stunting"],
    "Jumlah": [77, 808]
}

df_outcome = pd.DataFrame(data)

# === Visualisasi ===
plt.figure(figsize=(6, 5))
sns.barplot(x='Status', y='Jumlah', data=df_outcome, color='steelblue')

# Tambahkan label angka di atas batang
for index, row in df_outcome.iterrows():
    plt.text(index, row.Jumlah + 10, int(row.Jumlah), ha='center', va='bottom', fontsize=10)

# Format diagram
plt.title('Jumlah Data Outcome')
plt.ylabel('Count')
plt.xlabel('')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Tampilkan plot
plt.show()