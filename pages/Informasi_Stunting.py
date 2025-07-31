# pages/2_ℹ️_Informasi_Stunting.py
import streamlit as st
import sys
# Tambahkan path ke direktori utama agar bisa impor style_utils
sys.path.append('..')
import style_utils as su

su.inject_custom_css() # Terapkan CSS

st.title("Informasi Penting Mengenai Stunting")
st.image("https://asset.kompas.com/crops/fPWkvyugutU9RLjHuqZm0jPE-8g=/0x66:1000x566/1200x800/data/photo/2018/07/19/1775735881.jpg",
         caption="Sumber: lifestyle.kompas.com - Ukur Berat dan Tinggi Badan Anak Secara Rutin.")

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Apa Itu Stunting?")
st.markdown("""
Stunting adalah kondisi gagal tumbuh pada anak balita akibat kekurangan gizi kronis sehingga anak terlalu pendek untuk usianya.
""")
st.markdown('</div>', unsafe_allow_html=True)


st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Penyebab, Dampak, dan Pencegahan")
tab1, tab2, tab3 = st.tabs(["Penyebab", "Dampak", "Pencegahan"])
with tab1:
    st.markdown("""
    - **Asupan Gizi Kurang:** Terutama pada 1000 Hari Pertama Kehidupan.
    - **Pola Asuh Kurang Tepat:** Kurangnya pengetahuan ibu mengenai kesehatan dan gizi.
    - **Sanitasi dan Air Bersih:** Infeksi berulang akibat lingkungan tidak sehat.
    - **Akses Terbatas ke Layanan Kesehatan.**
    """)
with tab2:
    st.error("""
    - **Jangka Pendek:** Terganggunya perkembangan otak, kecerdasan, dan pertumbuhan fisik.
    - **Jangka Panjang:** Menurunnya kemampuan kognitif, kekebalan tubuh lemah, dan meningkatnya risiko penyakit kronis.
    """)
with tab3:
    st.success("""
    - **Penuhi Gizi Ibu Hamil.**
    - **ASI Eksklusif** selama 6 bulan.
    - **MPASI Berkualitas** setelah 6 bulan.
    - **Imunisasi Lengkap.**
    - **Pantau Pertumbuhan** secara teratur.
    - **Jaga Kebersihan** lingkungan.
    """)
st.markdown('</div>', unsafe_allow_html=True)