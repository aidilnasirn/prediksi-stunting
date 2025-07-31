from flask import Flask, render_template, request
import pandas  as pd
import numpy  as np
import pickle 


# import scikit.learn  as sk

app = Flask(__name__)

# --- Data Referensi WHO (LMS Parameters) ---
# Format: {usia_dalam_bulan: (L, M, S)}
# L = Skewness, M = Median, S = Coefficient of Variation
# PENTING: Ini adalah data sampel (0-24 bulan). Untuk aplikasi produksi, gunakan data lengkap 0-60 bulan dari WHO.

# Data Tinggi Badan menurut Usia (TB/U) - Laki-laki
DATA_TB_U_LAKI_LAKI = {
    0: (-0.5199, 49.9102, 0.03816), 1: (-0.3204, 54.7132, 0.03681),
    2: (-0.1557, 58.4234, 0.03565), 3: (-0.0379, 61.4305, 0.03483),
    4: (0.0465, 63.8999, 0.03423), 5: (0.1064, 65.9818, 0.03378),
    6: (0.1481, 67.7656, 0.03344), 7: (0.1762, 69.3093, 0.03318),
    8: (0.1942, 70.6611, 0.03298), 9: (0.2043, 71.8596, 0.03282),
    10: (0.2084, 72.9347, 0.03269), 11: (0.2078, 73.9085, 0.03258),
    12: (0.2037, 74.7993, 0.03249), 13: (0.1968, 75.6214, 0.03241),
    14: (0.1878, 76.3861, 0.03234), 15: (0.1771, 77.1018, 0.03228),
    16: (0.1652, 77.7753, 0.03223), 17: (0.1523, 78.4116, 0.03218),
    18: (0.1387, 79.0151, 0.03214), 19: (0.1246, 79.5891, 0.03211),
    20: (0.1102, 80.1367, 0.03208), 21: (0.0955, 80.6601, 0.03205),
    22: (0.0807, 81.1615, 0.03203), 23: (0.0658, 81.6425, 0.03201),
    24: (0.0510, 82.1047, 0.03199)
}

# Data Tinggi Badan menurut Usia (TB/U) - Perempuan
DATA_TB_U_PEREMPUAN = {
    0: (-0.5487, 49.1498, 0.03859), 1: (-0.3809, 53.7226, 0.03706),
    2: (-0.2185, 57.0678, 0.03592), 3: (-0.0993, 59.8037, 0.03513),
    4: (-0.0094, 62.0933, 0.03456), 5: (0.0601, 64.0453, 0.03415),
    6: (0.1136, 65.7383, 0.03385), 7: (0.1546, 67.2284, 0.03362),
    8: (0.1859, 68.5583, 0.03344), 9: (0.2095, 69.7606, 0.03330),
    10: (0.2269, 70.8601, 0.03318), 11: (0.2393, 71.8749, 0.03309),
    12: (0.2477, 72.8198, 0.03301), 13: (0.2529, 73.7058, 0.03295),
    14: (0.2555, 74.5414, 0.03289), 15: (0.2560, 75.3331, 0.03284),
    16: (0.2547, 76.0858, 0.03279), 17: (0.2521, 76.8041, 0.03274),
    18: (0.2482, 77.4912, 0.03270), 19: (0.2435, 78.1499, 0.03265),
    20: (0.2379, 78.7825, 0.03261), 21: (0.2317, 79.3913, 0.03257),
    22: (0.2249, 79.9781, 0.03253), 23: (0.2177, 80.5446, 0.03249),
    24: (0.2101, 81.0924, 0.03245)
}

# Data Berat Badan menurut Usia (BB/U) - Laki-laki
DATA_BB_U_LAKI_LAKI = {
    0: (-0.3547, 3.3243, 0.1030), 1: (-0.2062, 4.4727, 0.0917),
    2: (-0.0820, 5.6133, 0.0818), 3: (0.0163, 6.4024, 0.0761),
    4: (0.0863, 6.9934, 0.0726), 5: (0.1360, 7.4947, 0.0700),
    6: (0.1691, 7.9407, 0.0681), 7: (0.1895, 8.3496, 0.0667),
    8: (0.1997, 8.7291, 0.0657), 9: (0.2016, 9.0858, 0.0649),
    10: (0.1969, 9.4243, 0.0642), 11: (0.1869, 9.7479, 0.0637),
    12: (0.1729, 10.0592, 0.0632), 13: (0.1558, 10.3601, 0.0628),
    14: (0.1365, 10.6517, 0.0624), 15: (0.1158, 10.9348, 0.0621),
    16: (0.0942, 11.2104, 0.0618), 17: (0.0721, 11.4795, 0.0615),
    18: (0.0496, 11.7428, 0.0613), 19: (0.0270, 12.0009, 0.0610),
    20: (0.0044, 12.2544, 0.0608), 21: (-0.0180, 12.5037, 0.0606),
    22: (-0.0402, 12.7493, 0.0604), 23: (-0.0621, 12.9915, 0.0602),
    24: (-0.0837, 13.2307, 0.0600)
}

# Data Berat Badan menurut Usia (BB/U) - Perempuan
DATA_BB_U_PEREMPUAN = {
    0: (-0.4619, 3.2201, 0.1065), 1: (-0.3016, 4.1951, 0.0950),
    2: (-0.1706, 5.1432, 0.0863), 3: (-0.0700, 5.8643, 0.0809),
    4: (0.0016, 6.4253, 0.0775), 5: (0.0537, 6.8906, 0.0751),
    6: (0.0912, 7.2940, 0.0733), 7: (0.1171, 7.6534, 0.0719),
    8: (0.1343, 7.9781, 0.0708), 9: (0.1444, 8.2743, 0.0699),
    10: (0.1485, 8.5469, 0.0692), 11: (0.1477, 8.8000, 0.0686),
    12: (0.1432, 9.0360, 0.0681), 13: (0.1357, 9.2570, 0.0676),
    14: (0.1257, 9.4649, 0.0672), 15: (0.1137, 9.6609, 0.0668),
    16: (0.1002, 9.8462, 0.0665), 17: (0.0855, 10.0216, 0.0662),
    18: (0.0699, 10.1878, 0.0659), 19: (0.0536, 10.3455, 0.0656),
    20: (0.0368, 10.4953, 0.0654), 21: (0.0196, 10.6378, 0.0651),
    22: (0.0022, 10.7735, 0.0649), 23: (-0.0154, 10.9029, 0.0647),
    24: (-0.0331, 11.0264, 0.0645)
}


def hitung_zscore(jenis_kelamin, usia, pengukuran, data_referensi):
    """
    Menghitung Z-score menggunakan formula LMS.
    Args:
        jenis_kelamin (str): 'laki-laki' atau 'perempuan'.
        usia (int): Usia anak dalam bulan.
        pengukuran (float): Nilai pengukuran (tinggi badan atau berat badan).
        data_referensi (dict): Data referensi WHO (L, M, S) untuk indikator tertentu.
    Returns:
        tuple: (z_score, error_message)
    """
    if usia not in data_referensi:
        return None, "Data usia di luar rentang (0-24 bulan)."

    L, M, S = data_referensi[usia]
    
    # Menghitung Z-score
    if L == 0: # Jika L = 0, gunakan formula khusus untuk L=0
        z_score = (pengukuran / M) ** (1 / S) - 1
    else:
        z_score = (((pengukuran / M) ** L) - 1) / (L * S)
    
    return z_score, None

def klasifikasi_stunting(z_score_tb_u):
    """
    Memberikan klasifikasi status gizi berdasarkan Z-score Tinggi Badan menurut Usia (TB/U).
    Args:
        z_score_tb_u (float): Z-score TB/U.
    Returns:
        tuple: (status, deskripsi)
    """
    if z_score_tb_u is None:
        return "Tidak dapat diklasifikasikan", "Data TB/U tidak valid."
        
    if z_score_tb_u < -3:
        status = "Sangat Pendek (Severely Stunted)"
        deskripsi = "Anak Anda terindikasi stunting berat. Segera konsultasikan dengan dokter atau ahli gizi untuk penanganan lebih lanjut."
    elif -3 <= z_score_tb_u < -2:
        status = "Pendek (Stunted)"
        deskripsi = "Anak Anda terindikasi stunting. Disarankan untuk berkonsultasi dengan tenaga kesehatan untuk memantau pertumbuhan dan mendapatkan saran gizi yang tepat."
    elif z_score_tb_u > 2:
        status = "Tinggi"
        deskripsi = "Tinggi badan anak Anda berada di atas rata-rata anak seusianya. Ini umumnya adalah pertanda baik."
    else: # -2 <= z_score_tb_u <= 2
        status = "Normal"
        deskripsi = "Selamat! Status gizi anak Anda berdasarkan tinggi badan menurut usia adalah normal. Terus pertahankan pola makan bergizi seimbang."
        
    return status, deskripsi

def klasifikasi_bb_u(z_score_bb_u):
    """
    Memberikan klasifikasi status gizi berdasarkan Z-score Berat Badan menurut Usia (BB/U).
    Args:
        z_score_bb_u (float): Z-score BB/U.
    Returns:
        tuple: (status, deskripsi)
    """
    if z_score_bb_u is None:
        return "Tidak dapat diklasifikasikan", "Data BB/U tidak valid."

    if z_score_bb_u < -3:
        status = "Sangat Kurus (Severely Underweight)"
        deskripsi = "Berat badan anak Anda sangat kurang. Ini memerlukan perhatian medis segera."
    elif -3 <= z_score_bb_u < -2:
        status = "Kurus (Underweight)"
        deskripsi = "Berat badan anak Anda kurang. Disarankan untuk memantau asupan gizi dan berkonsultasi dengan tenaga kesehatan."
    elif -2 <= z_score_bb_u <= 1:
        status = "Normal"
        deskripsi = "Berat badan anak Anda normal untuk usianya. Pertahankan pola makan sehat."
    elif 1 < z_score_bb_u <= 2:
        status = "Berisiko Gizi Lebih (Risk of Overweight)"
        deskripsi = "Anak Anda berisiko mengalami gizi lebih. Perhatikan pola makan dan aktivitas fisiknya."
    elif 2 < z_score_bb_u <= 3:
        status = "Gizi Lebih (Overweight)"
        deskripsi = "Anak Anda terindikasi gizi lebih. Konsultasikan dengan ahli gizi untuk penyesuaian pola makan."
    else: # z_score_bb_u > 3
        status = "Obesitas (Obese)"
        deskripsi = "Anak Anda terindikasi obesitas. Segera konsultasikan dengan ahli gizi dan dokter untuk penanganan komprehensif."
    
    return status, deskripsi


@app.route('/')
def index():
    """Menampilkan halaman utama."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """Memproses data input dan menampilkan hasil prediksi."""
    try:
        nama_anak = request.form['nama_anak']
        usia = int(request.form['usia'])
        jenis_kelamin = request.form['jenis_kelamin']
        berat_badan = float(request.form['berat_badan']) # Menambahkan input berat badan
        tinggi_badan = float(request.form['tinggi_badan'])

        # Validasi sederhana
        if not (0 <= usia <= 24):
            raise ValueError("Usia harus antara 0 dan 24 bulan untuk data saat ini.")
        if not (2.0 <= berat_badan <= 25.0): # Rentang berat badan yang lebih realistis
            raise ValueError("Berat badan tidak wajar, pastikan dalam kilogram (kg).")
        if not (40 <= tinggi_badan <= 120):
            raise ValueError("Tinggi badan tidak wajar, pastikan dalam sentimeter (cm).")

        # Hitung Z-score TB/U
        data_ref_tb_u = DATA_TB_U_LAKI_LAKI if jenis_kelamin == 'laki-laki' else DATA_TB_U_PEREMPUAN
        z_score_tb_u, error_tb_u = hitung_zscore(jenis_kelamin, usia, tinggi_badan, data_ref_tb_u)
        
        if error_tb_u:
            raise ValueError(error_tb_u)

        # Klasifikasi status TB/U
        status_tb_u, deskripsi_tb_u = klasifikasi_stunting(z_score_tb_u)

        # Hitung Z-score BB/U
        data_ref_bb_u = DATA_BB_U_LAKI_LAKI if jenis_kelamin == 'laki-laki' else DATA_BB_U_PEREMPUAN
        z_score_bb_u, error_bb_u = hitung_zscore(jenis_kelamin, usia, berat_badan, data_ref_bb_u)

        if error_bb_u:
            raise ValueError(error_bb_u)

        # Klasifikasi status BB/U
        status_bb_u, deskripsi_bb_u = klasifikasi_bb_u(z_score_bb_u)

        return render_template('result.html', 
                               nama_anak=nama_anak,
                               usia=usia,
                               jenis_kelamin=jenis_kelamin.capitalize(),
                               tinggi_badan=tinggi_badan,
                               berat_badan=berat_badan, # Kirim berat badan ke template
                               z_score_tb_u=round(z_score_tb_u, 2),
                               status_tb_u=status_tb_u,
                               deskripsi_tb_u=deskripsi_tb_u,
                               z_score_bb_u=round(z_score_bb_u, 2), # Kirim z-score BB/U
                               status_bb_u=status_bb_u, # Kirim status BB/U
                               deskripsi_bb_u=deskripsi_bb_u) # Kirim deskripsi BB/U

    except (ValueError, KeyError) as e:
        # Menangani error jika input tidak valid atau field kosong
        return render_template('index.html', error=f"Terjadi Kesalahan: {e}. Pastikan semua kolom terisi dengan benar.")


if __name__ == '__main__':
    app.run(debug=True)
