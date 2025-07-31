import streamlit as st
import style_utils as su  # Impor utilitas style

st.set_page_config(
    page_title="Prediksi Stunting",
    page_icon="",
    layout="centered",
    initial_sidebar_state="expanded"
)
su.inject_custom_css()  # Terapkan CSS

st.markdown('<div class="card">', unsafe_allow_html=True)
st.title("Selamat Datang!")
st.markdown("""
Aplikasi ini dirancang untuk membantu Anda memantau status gizi anak (usia 0-24 bulan)
berdasarkan **Standar Pertumbuhan Anak dari WHO**.

### Fitur Utama:
- **Kalkulator Gizi**: Hitung Z-Score untuk Tinggi Badan dan Berat Badan.
- **Informasi Stunting**: Pelajari tentang stunting, penyebab, dan pencegahannya.

**👈 Silakan pilih halaman dari menu di samping untuk memulai.**
""")
st.markdown('</div>', unsafe_allow_html=True)

st.info("Aplikasi ini bersifat edukatif dan tidak menggantikan konsultasi medis profesional.")