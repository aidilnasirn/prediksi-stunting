import streamlit as st

def inject_custom_css():
    """
    Fungsi untuk membaca file style.css dan menyisipkannya
    ke dalam aplikasi Streamlit.
    """
    try:
        with open("style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.error("File 'style.css' tidak ditemukan. Pastikan file tersebut ada di direktori yang sama.")