# pages/1_🧮_Kalkulator_Gizi.py
import streamlit as st
import numpy as np
import sys
# Tambahkan path ke direktori utama agar bisa impor style_utils
sys.path.append('..')
import style_utils as su

# --- BAGIAN DATA DAN FUNGSI PERHITUNGAN ---
# (Salin semua kamus data dan fungsi perhitungan dari kode Anda sebelumnya ke sini)
# ... KODE DATA DAN FUNGSI ANDA DI SINI ...
# --- AKHIR BAGIAN DATA DAN FUNGSI ---

# --- UI ---
su.inject_custom_css() # Terapkan CSS

st.title("Kalkulator Status Gizi Anak")
st.markdown('<div class="card">', unsafe_allow_html=True)

with st.form(key="gizi_form"):
    st.subheader("Masukkan Data Anak")
    # ... (sisa kode form sama seperti sebelumnya) ...
    nama_anak = st.text_input("Nama Anak", placeholder="Contoh: Budi")
    usia = st.number_input("Usia (bulan)", 0, 24, 12, help="Usia 0-24 bulan.")
    berat_badan = st.number_input("Berat Badan (kg)", 1.0, 25.0, 9.6, 0.1, format="%.1f")
    jenis_kelamin = st.radio("Jenis Kelamin", ["Laki-laki", "Perempuan"], horizontal=True)
    tinggi_badan = st.number_input("Tinggi Badan (cm)", 40.0, 120.0, 75.0, 0.1, format="%.1f")

    submitted = st.form_submit_button("Analisis Sekarang", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

if submitted:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    # ... (sisa kode logika setelah submit sama seperti sebelumnya) ...
    # Pastikan Anda sudah menyalinnya dengan benar
    st.markdown('</div>', unsafe_allow_html=True)