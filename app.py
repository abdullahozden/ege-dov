import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(page_title="Karakter Patakla", layout="centered")

# --- RESMİ KODA DÖNÜŞTÜRME (BASE64) ---
def get_image_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# DOSYA ADI KONTROLÜ (Burası Çok Önemli!)
# GitHub'a yüklediğin resmin adı neyse tam olarak onu yaz (Örn: karakter.png)
resim_adi = "ege.png" 

if os.path.exists(resim_adi):
    img_base64 = get_image_base64(resim_adi)
    img_data = f"data:image/png;base64,{img_base64}"
    
    # HTML dosyasını oku
    with open("oyun.html", "r", encoding="utf-8") as f:
        html_kodu = f.read()
    
    # HTML içindeki boş src kısmına resmi enjekte et
    html_kodu = html_kodu.replace('id="karakter" src=""', f'id="karakter" src="{img_data}"')
    
    st.title("🕹️ Karakterini Patakla!")
    components.html(html_kodu, height=650)
else:
    st.error(f"Hata: '{resim_adi}' dosyası bulunamadı! Lütfen resmi GitHub'a yüklediğinden emin ol.")
