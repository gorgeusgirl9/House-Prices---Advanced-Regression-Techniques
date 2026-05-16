* **Problem:** Konutların yapısal (m², oda/banyo sayısı, bina yaşı) ve konumsal özelliklerine göre piyasa satış değerlerini tahmin etmek.
* **Algoritma:** `GradientBoostingRegressor` (Ardışık Öğrenme Mimarisi)
* **Metrik & Başarı:** Yüksek tahmin ve açıklayıcılık gücüne sahip kararlı **$R^2$ Skoru**.
* **Mühendislik:** Sürekli ve kategorik gayrimenkul öznitelikleri, cari piyasa çarpanları ve yıpranma payları dikkate alınarak doğrusal olmayan fiyat trendlerine göre ölçeklenmiştir.

-
