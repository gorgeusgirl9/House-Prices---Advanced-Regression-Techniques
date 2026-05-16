# 🏎️ Üretim Bandı Test Süresi & 🏠 Ev Fiyatları Gelişmiş Regresyon Projeleri

Bu depo, endüstriyel üretim optimizasyonu ve gayrimenkul değerleme alanlarında geliştirilmiş iki adet gelişmiş makine öğrenmesi regresyon modelini içermektedir.

---

## 📊 9. Proje: Mercedes-Benz Greener Manufacturing

* **Problem:** Araçların fabrikasyon donanım özelliklerine göre güvenlik test sürelerini saniye cinsinden tahmin etmek.
* **Algoritma:** Scikit-Learn `RandomForestRegressor`
* **Metrik & Başarı:** **0.7538 $R^2$ Skoru** (Açıklayıcılık Gücü).
* **Mühendislik:** Çok boyutlu ve anonim endüstriyel tablo verileri, gürültü parametreleri yönetilerek gerçeğe en yakın doğrusal olmayan yapıda simüle edilmiştir.

---

## 📊 10. Proje: House Prices - Advanced Regression Techniques

* **Problem:** Konutların yapısal (m², oda/banyo sayısı, bina yaşı) ve konumsal özelliklerine göre piyasa satış değerlerini tahmin etmek.
* **Algoritma:** `GradientBoostingRegressor` (Ardışık Öğrenme Mimarisi)
* **Metrik & Başarı:** Yüksek tahmin ve açıklayıcılık gücüne sahip kararlı **$R^2$ Skoru**.
* **Mühendislik:** Sürekli ve kategorik gayrimenkul öznitelikleri, cari piyasa çarpanları ve yıpranma payları dikkate alınarak doğrusal olmayan fiyat trendlerine göre ölçeklenmiştir.

---

## 🚀 Canlı Uygulamalar (Deployment)

Her iki proje de kullanıcı dostu arayüzlerle **Hugging Face Spaces** üzerinde **Streamlit** mimarisi kullanılarak canlıya alınmıştır. 
* **Mercedes-Benz Test Süresi Arayüzü:** Araç donanım paketlerine göre üretim bandı akış analizi yapar.
* **Ev Fiyat Tahmin Arayüzü:** Yapısal ve coğrafi verilere göre anlık yapay zeka tabanlı ekspertiz raporu üretir.
