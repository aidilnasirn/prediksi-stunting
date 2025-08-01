import streamlit as st
import numpy as np

def inject_custom_css():
    """
    Fungsi untuk membaca file style.css dan menyisipkannya.
    Ini disalin ke sini agar file ini mandiri dan mudah dijalankan.
    """
    try:
        with open("style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("File 'style.css' tidak ditemukan.")

# --- BAGIAN DATA DAN FUNGSI PERHITUNGAN (Lengkap) ---
DATA_TB_U_LAKI_LAKI = {
    0: (-0.5199, 49.9102, 0.03816), 1: (-0.3204, 54.7132, 0.03681), 2: (-0.1557, 58.4234, 0.03565),
    3: (-0.0379, 61.4305, 0.03483), 4: (0.0465, 63.8999, 0.03423), 5: (0.1064, 65.9818, 0.03378),
    6: (0.1481, 67.7656, 0.03344), 7: (0.1762, 69.3093, 0.03318), 8: (0.1942, 70.6611, 0.03298),
    9: (0.2043, 71.8596, 0.03282), 10: (0.2084, 72.9347, 0.03269), 11: (0.2078, 73.9085, 0.03258),
    12: (0.2037, 74.7993, 0.03249), 13: (0.1968, 75.6214, 0.03241), 14: (0.1878, 76.3861, 0.03234),
    15: (0.1771, 77.1018, 0.03228), 16: (0.1652, 77.7753, 0.03223), 17: (0.1523, 78.4116, 0.03218),
    18: (0.1387, 79.0151, 0.03214), 19: (0.1246, 79.5891, 0.03211), 20: (0.1102, 80.1367, 0.03208),
    21: (0.0955, 80.6601, 0.03205), 22: (0.0807, 81.1615, 0.03203), 23: (0.0658, 81.6425, 0.03201),
    24: (0.0510, 82.1047, 0.03199)
}
DATA_TB_U_PEREMPUAN = {
    0: (-0.5487, 49.1498, 0.03859), 1: (-0.3809, 53.7226, 0.03706), 2: (-0.2185, 57.0678, 0.03592),
    3: (-0.0993, 59.8037, 0.03513), 4: (-0.0094, 62.0933, 0.03456), 5: (0.0601, 64.0453, 0.03415),
    6: (0.1136, 65.7383, 0.03385), 7: (0.1546, 67.2284, 0.03362), 8: (0.1859, 68.5583, 0.03344),
    9: (0.2095, 69.7606, 0.03330), 10: (0.2269, 70.8601, 0.03318), 11: (0.2393, 71.8749, 0.03309),
    12: (0.2477, 72.8198, 0.03301), 13: (0.2529, 73.7058, 0.03295), 14: (0.2555, 74.5414, 0.03289),
    15: (0.2560, 75.3331, 0.03284), 16: (0.2547, 76.0858, 0.03279), 17: (0.2521, 76.8041, 0.03274),
    18: (0.2482, 77.4912, 0.03270), 19: (0.2435, 78.1499, 0.03265), 20: (0.2379, 78.7825, 0.03261),
    21: (0.2317, 79.3913, 0.03257), 22: (0.2249, 79.9781, 0.03253), 23: (0.2177, 80.5446, 0.03249),
    24: (0.2101, 81.0924, 0.03245)
}
DATA_BB_U_LAKI_LAKI = {
    0: (-0.3547, 3.3243, 0.1030), 1: (-0.2062, 4.4727, 0.0917), 2: (-0.0820, 5.6133, 0.0818),
    3: (0.0163, 6.4024, 0.0761), 4: (0.0863, 6.9934, 0.0726), 5: (0.1360, 7.4947, 0.0700),
    6: (0.1691, 7.9407, 0.0681), 7: (0.1895, 8.3496, 0.0667), 8: (0.1997, 8.7291, 0.0657),
    9: (0.2016, 9.0858, 0.0649), 10: (0.1969, 9.4243, 0.0642), 11: (0.1869, 9.7479, 0.0637),
    12: (0.1729, 10.0592, 0.0632), 13: (0.1558, 10.3601, 0.0628), 14: (0.1365, 10.6517, 0.0624),
    15: (0.1158, 10.9348, 0.0621), 16: (0.0942, 11.2104, 0.0618), 17: (0.0721, 11.4795, 0.0615),
    18: (0.0496, 11.7428, 0.0613), 19: (0.0270, 12.0009, 0.0610), 20: (0.0044, 12.2544, 0.0608),
    21: (-0.0180, 12.5037, 0.0606), 22: (-0.0402, 12.7493, 0.0604), 23: (-0.0621, 12.9915, 0.0602),
    24: (-0.0837, 13.2307, 0.0600)
}
DATA_BB_U_PEREMPUAN = {
    0: (-0.4619, 3.2201, 0.1065), 1: (-0.3016, 4.1951, 0.0950), 2: (-0.1706, 5.1432, 0.0863),
    3: (-0.0700, 5.8643, 0.0809), 4: (0.0016, 6.4253, 0.0775), 5: (0.0537, 6.8906, 0.0751),
    6: (0.0912, 7.2940, 0.0733), 7: (0.1171, 7.6534, 0.0719), 8: (0.1343, 7.9781, 0.0708),
    9: (0.1444, 8.2743, 0.0699), 10: (0.1485, 8.5469, 0.0692), 11: (0.1477, 8.8000, 0.0686),
    12: (0.1432, 9.0360, 0.0681), 13: (0.1357, 9.2570, 0.0676), 14: (0.1257, 9.4649, 0.0672),
    15: (0.1137, 9.6609, 0.0668), 16: (0.1002, 9.8462, 0.0665), 17: (0.0855, 10.0216, 0.0662),
    18: (0.0699, 10.1878, 0.0659), 19: (0.0536, 10.3455, 0.0656), 20: (0.0368, 10.4953, 0.0654),
    21: (0.0196, 10.6378, 0.0651), 22: (0.0022, 10.7735, 0.0649), 23: (-0.0154, 10.9029, 0.0647),
    24: (-0.0331, 11.0264, 0.0645)
}

def hitung_zscore(usia, pengukuran, data_referensi):
    if usia not in data_referensi:
        raise ValueError(f"Data untuk usia {usia} bulan tidak tersedia.")
    L, M, S = data_referensi[usia]
    if L == 0:
        return np.log(pengukuran / M) / S
    else:
        return (((pengukuran / M) ** L) - 1) / (L * S)

def klasifikasi_stunting(z_score):
    if z_score < -3: return "Sangat Pendek (Severely Stunted)", "error"
    if -3 <= z_score < -2: return "Pendek (Stunted)", "warning"
    if z_score > 2: return "Tinggi", "info"
    return "Normal", "success"

def get_deskripsi_stunting(status):
    if status == "Sangat Pendek (Severely Stunted)": return "Anak Anda terindikasi stunting berat. **Segera konsultasikan dengan dokter atau ahli gizi.**"
    if status == "Pendek (Stunted)": return "Anak Anda terindikasi stunting. Disarankan untuk berkonsultasi dengan tenaga kesehatan untuk pemantauan."
    if status == "Tinggi": return "Tinggi badan anak Anda berada di atas rata-rata. Ini umumnya pertanda baik."
    return "Selamat! Tinggi badan anak Anda normal. Terus pertahankan pola makan bergizi seimbang."

def klasifikasi_bb_u(z_score):
    if z_score < -3: return "Berat Badan Sangat Kurang", "error"
    if -3 <= z_score < -2: return "Berat Badan Kurang", "warning"
    if 1 < z_score <= 2: return "Berisiko Gizi Lebih", "warning"
    if 2 < z_score <= 3: return "Gizi Lebih", "error"
    if z_score > 3: return "Obesitas", "error"
    return "Berat Badan Normal", "success"

def get_deskripsi_bb_u(status):
    if status == "Berat Badan Sangat Kurang": return "Berat badan anak Anda sangat kurang. **Ini memerlukan perhatian medis segera.**"
    if status == "Berat Badan Kurang": return "Berat badan anak Anda kurang. Disarankan untuk memantau asupan gizi."
    if status == "Berisiko Gizi Lebih": return "Anak Anda berisiko mengalami gizi lebih. Perhatikan pola makan dan aktivitas fisiknya."
    if status == "Gizi Lebih": return "Anak Anda terindikasi gizi lebih. Konsultasikan dengan ahli gizi untuk penyesuaian pola makan."
    if status == "Obesitas": return "Anak Anda terindikasi obesitas. Segera konsultasikan dengan ahli gizi dan dokter."
    return "Berat badan anak Anda normal untuk usianya. Pertahankan pola makan sehat."

# --- ANTARMUKA STREAMLIT (UI) ---
inject_custom_css()

st.title("Kalkulator Status Gizi Anak")
st.markdown('<div class="card">', unsafe_allow_html=True)

with st.form(key="gizi_form"):
    st.subheader("Masukkan Data Anak")
    col1, col2 = st.columns(2)
    with col1:
        nama_anak = st.text_input("Nama Anak", placeholder="Contoh: Budi")
        usia = st.number_input("Usia (bulan)", 0, 24, 12, help="Usia 0-24 bulan.")
    with col2:
        jenis_kelamin = st.radio("Jenis Kelamin", ["Laki-laki", "Perempuan"], horizontal=True)
        tinggi_badan = st.number_input("Tinggi Badan (cm)", 40.0, 120.0, 75.0, 0.1, format="%.1f")
    
    berat_badan = st.number_input("Berat Badan (kg)", 1.0, 25.0, 9.6, 0.1, format="%.1f")
    submitted = st.form_submit_button("Analisis Sekarang", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# == BAGIAN YANG DIPERBAIKI ADA DI BAWAH INI ==
if submitted:
    if not nama_anak:
        st.error("Nama anak harus diisi.")
    else:
        try:
            # Bungkus hasil dalam sebuah kartu (card)
            st.markdown('<div class="card">', unsafe_allow_html=True)
            
            # Persiapan data
            jk_key = 'laki-laki' if jenis_kelamin == "Laki-laki" else 'perempuan'

            # 1. Perhitungan Tinggi Badan (TB/U)
            data_ref_tb = DATA_TB_U_LAKI_LAKI if jk_key == 'laki-laki' else DATA_TB_U_PEREMPUAN
            z_tb = hitung_zscore(usia, tinggi_badan, data_ref_tb)
            status_tb, tipe_tb = klasifikasi_stunting(z_tb)
            desk_tb = get_deskripsi_stunting(status_tb)

            # 2. Perhitungan Berat Badan (BB/U)
            data_ref_bb = DATA_BB_U_LAKI_LAKI if jk_key == 'laki-laki' else DATA_BB_U_PEREMPUAN
            z_bb = hitung_zscore(usia, berat_badan, data_ref_bb)
            status_bb, tipe_bb = klasifikasi_bb_u(z_bb)
            desk_bb = get_deskripsi_bb_u(status_bb)

            # 3. Tampilkan Hasil
            st.header(f"Hasil Analisis untuk {nama_anak.title()}")
            st.write(f"Usia: {usia} bulan | Jenis Kelamin: {jenis_kelamin} | TB: {tinggi_badan} cm | BB: {berat_badan} kg")
            st.markdown("---")

            col1, col2 = st.columns(2)
            with col1:
                st.subheader("Status Tinggi Badan")
                st.metric("Z-Score (TB/U)", f"{z_tb:.2f}")
                if tipe_tb == 'error': st.error(f"**{status_tb}**")
                elif tipe_tb == 'warning': st.warning(f"**{status_tb}**")
                elif tipe_tb == 'info': st.info(f"**{status_tb}**")
                else: st.success(f"**{status_tb}**")
                with st.expander("Lihat Rekomendasi"):
                    st.write(desk_tb)

            with col2:
                st.subheader("Status Berat Badan")
                st.metric("Z-Score (BB/U)", f"{z_bb:.2f}")
                if tipe_bb == 'error': st.error(f"**{status_bb}**")
                elif tipe_bb == 'warning': st.warning(f"**{status_bb}**")
                else: st.success(f"**{status_bb}**")
                with st.expander("Lihat Rekomendasi"):
                    st.write(desk_bb)
            
            st.markdown('</div>', unsafe_allow_html=True)

        except ValueError as e:
            st.error(f"Gagal melakukan analisis: {e}")
