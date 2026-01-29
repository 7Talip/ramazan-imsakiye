# 🌙 Ramazan İmsakiye & İftar Geri Sayım Uygulaması

Bu proje, Türkiye şehirleri için **imsakiye bilgilerini** otomatik olarak çekip
**bugünün imsakiyesi** ve **iftara ne kadar kaldığını** gösteren bir **Streamlit web uygulamasıdır**.

Canlı olarak web üzerinde çalışır ve herhangi bir kurulum gerektirmez.

---

## 🚀 Özellikler

- 📍 Şehir seçimine göre imsakiye
- 📅 Günlük imsakiye tablosu
- ⏱ İftara ne kadar kaldı hesabı
- 🕰 Zaman bazlı `datetime` hesaplamaları
- 🌐 Web tabanlı (Streamlit)
- ☁️ Streamlit Cloud üzerinden deploy edilebilir

---

## 🛠 Kullanılan Teknolojiler

- Python 3
- Pandas
- Streamlit
- datetime
- HTML tablo parsing (`pd.read_html`)

---

## 📂 Proje Yapısı

ramazan-imsakiye/
├── main.py
├── requirements.txt
└── README.md

---

## 📦 Kurulum (Lokal)

```bash
git clone https://github.com/kullanici-adi/ramazan-imsakiye.git
cd ramazan-imsakiye
pip install -r requirements.txt
streamlit run main.py
```

---

## ☁️ Streamlit Cloud Üzerinde Çalıştırma

1. Repo’yu GitHub’a yükle
2. https://share.streamlit.io adresine git
3. New App → repo’yu seç
4. main.py dosyasını işaretle
5. Deploy 🚀

---

## 🧠 Çalışma Mantığı (Özet)

- İmsakiye verileri pd.read_html ile web’den çekilir
- Gün / Ay / Yıl bilgisi ayrıştırılır
- Ay isimleri numerik değerlere çevrilir
- datetime nesnesi oluşturulur
- Bugünün verisi filtrelenir
- İftar vakti ile şu an arasındaki süre hesaplanır

---

## ⚠️ Notlar

- Tarih sütunu hesaplama için datetime olarak tutulur
- Kullanıcıya gösterirken sadece gün.ay.yıl formatında sunulur
- Uygulama Ramazan dışı günlerde veri bulunamadı uyarısı verir

---

## 👤 Geliştirici

Bu proje öğrenme, veri işleme ve web uygulaması geliştirme amaçlı hazırlanmıştır.
Geri bildirim ve katkılara açıktır.

---

## 🌙 Hayırlı Ramazanlar

---



