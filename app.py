import streamlit as st
import streamlit.components.v1 as components

# Sayfa ayarları
st.set_page_config(page_title="Karakter Patakla", layout="centered")

# HTML dosyasını oku
with open("oyun.html", "r", encoding="utf-8") as f:
    html_kodu = f.read()

# HTML'i Streamlit içinde göster
st.title("🕹️ Karakterini Patakla!")
components.html(html_kodu, height=650, scrolling=False)

st.info("Karaktere tıklayarak vurabilirsin!")
