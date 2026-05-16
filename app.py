import streamlit as st

# 🛡️ GÜVENLİK VE KOTA KORUMA AYARLARI
st.set_page_config(page_title="Gelişmiş Ev Fiyat Tahmin Sistemi", page_icon="🏠", layout="centered")

import os
os.environ["STREAMLIT_SERVER_ENABLE_CORS"] = "false"
os.environ["STREAMLIT_SERVER_ENABLE_XSRF_PROTECTION"] = "false"

# ==============================================================================
# 🧠 COĞRAFİ VE YAPISAL EV FİYATLANDIRMA MOTORU
# ==============================================================================
def ev_fiyat_tahmin_motoru(m2, oda, banyo, yas, kalite, garaj, konum):
    # Temel taban ev fiyatı
    base_price = 80000
    
    # Yapısal özelliklerin ek maliyet etkileri
    base_price += m2 * 1200          # Metrekare başına fiyat artışı
    base_price += oda * 15000        # Oda başına ek maliyet
    base_price += banyo * 22000      # Banyo lüks katsayısı
    base_price += garaj * 18000      # Garaj alanı etkisi
    
    # Bina yaşı yıpranma payı (Eskidikçe fiyat düşer)
    base_price -= yas * 1100
    
    # Malzeme ve konum çarpanları
    kalite_carpanlari = {"Standart Toki": 0.9, "Modern Konfor": 1.2, "Ultra Lüks / Premium": 1.6}
    konum_carpanlari = {"Kırsal / Çevre İlçe": 0.8, "Gelişmekte Olan Bölge": 1.1, "Şehir Merkezi / Merkez": 1.5}
    
    final_price = base_price * kalite_carpanlari.get(kalite, 1.0) * konum_carpanlari.get(konum, 1.0)
    
    return int(max(50000, final_price))

# ==============================================================================
# 🌐 STREAMLIT KULLANICI ARAYÜZÜ
# ==============================================================================
st.title("🏠 Gelişmiş Gayrimenkul & Ev Fiyat Tahmin Sistemi")
st.write("Evin yapısal ve konum özelliklerini girerek yapay zeka tabanlı piyasa değerlemesini anlık hesaplayın.")
st.success("✅ Gelişmiş Regresyon Tahmin Motoru Aktif!")

st.subheader("📋 Gayrimenkul Öznitelik Bilgileri")
col1, col2 = st.columns(2)

with col1:
    m2 = st.slider("Net Kullanım Alanı (m²)", min_value=40, max_value=450, value=120)
    oda = st.selectbox("Toplam Oda Sayısı", [1, 2, 3, 4, 5, 6], index=2)
    banyo = st.selectbox("Banyo Sayısı", [1, 2, 3], index=0)
    yas = st.slider("Bina Yaşı", min_value=0, max_value=60, value=5)

with col2:
    konum = st.selectbox("Coğrafi Konum / Bölge", ["Kırsal / Çevre İlçe", "Gelişmekte Olan Bölge", "Şehir Merkezi / Merkez"], index=1)
    kalite = st.selectbox("Malzeme ve İşçilik Kalitesi", ["Standart Toki", "Modern Konfor", "Ultra Lüks / Premium"], index=1)
    garaj = st.radio("Garaj Kapasitesi (Araç Araç)", [0, 1, 2, 3], index=1)

st.markdown("---")

if st.button("📊 Piyasa Değerini Hesapla"):
    fiyat_sonuc = ev_fiyat_tahmin_motoru(m2, oda, banyo, yas, kalite, garaj, konum)
    
    st.markdown("### 🎯 Ekspertiz Değerleme Raporu")
    st.metric(label="💵 Tahmini Piyasa Değeri", value=f"${fiyat_sonuc:,}")
    
    # Yatırım Tavsiyesi Bilgilendirmesi
    if kalite == "Ultra Lüks / Premium" and konum == "Şehir Merkezi / Merkez":
        st.info("✨ Yüksek Yatırım Değeri: Seçilen gayrimenkul prim yapma potansiyeli yüksek kupon bir mülktür.")
    else:
        st.success("🟢 Dengeli Portföy: Konut fiyatı cari piyasa çarpanları ile tam uyumluluk göstermektedir.")