import pandas as pd

# Data yang dimasukkan kembali, dengan usia dalam bulan
data_bulan = [
    ["Mei", 24, "Laki-laki", 12, 85, "Tidak"],
    ["Mei", 36, "Perempuan", 14, 90, "Ya"],
    ["Desember", 24, "Laki-laki", 11, 80, "Tidak"],
    ["Desember", 48, "Perempuan", 15, 95, "Ya"],
    ["April", 36, "Laki-laki", 13, 88, "Tidak"],
    ["April", 24, "Perempuan", 12, 84, "Ya"],
    ["November", 36, "Laki-laki", 14, 89, "Tidak"],
    ["November", 48, "Perempuan", 16, 92, "Ya"],
    ["Oktober", 24, "Laki-laki", 10, 78, "Ya"],
    ["Juli", 36, "Perempuan", 13, 87, "Tidak"],
    ["Agustus", 24, "Laki-laki", 11, 82, "Tidak"],
    ["Maret", 48, "Perempuan", 15, 94, "Ya"],
    ["September", 36, "Laki-laki", 14, 90, "Tidak"]
]

# Kolom-kolom tabel
columns_bulan = ["Bulan", "Usia (Bulan)", "Jenis Kelamin", "Berat Badan (kg)", "Tinggi Badan (cm)", "Stunting (Ya/Tidak)"]

# Buat DataFrame
df_bulan = pd.DataFrame(data_bulan, columns=columns_bulan)

# Simpan ke file Excel
new_file_path = "/mnt/data/Data_Stunting_Per_Bulan_Usia_Dalam_Bulan.xlsx"
df_bulan.to_excel(new_file_path, index=False)

new_file_path