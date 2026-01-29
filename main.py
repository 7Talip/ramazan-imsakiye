import pandas as pd
import numpy as np
from datetime import datetime
import streamlit as st

def imsakiye(sehir):
  ramazan = pd.read_html(f"https://www.sabah.com.tr/imsakiye/{sehir}")[0]
  ramazan = ramazan.drop("Unnamed: 0", axis=1)

  tarih = ramazan["Tarihler/ Günler"].str.split(" ", expand=True)
  tarih.columns = ["Gün", "Ay", "Haftanın_Günü"]

  tarih = tarih.drop(columns="Haftanın_Günü")

  tarih["Yıl"] = 2026

  ay_map = {
      "Ocak": 1, "Şubat": 2, "Mart": 3, "Nisan": 4,
      "Mayıs": 5, "Haziran": 6, "Temmuz": 7, "Ağustos": 8,
      "Eylül": 9, "Ekim": 10, "Kasım": 11, "Aralık": 12
  }

  tarih["Ay"] = tarih["Ay"].str.strip().map(ay_map)

  tarih["Tarih"] = pd.to_datetime(
      dict(
          year=tarih["Yıl"],
          month=tarih["Ay"],
          day=tarih["Gün"]
      )
  )

  ramazan["Tarih"] = tarih["Tarih"]
  ramazan = ramazan.drop(columns="Tarihler/ Günler")
  return ramazan

def iftara_ne_kadar_kaldi(sehir):
    df = imsakiye(sehir)

    now = datetime.now()
    today = pd.to_datetime(now.date())

    # Bugünün kaydı
    bugun = df[df["Tarih"] == today]

    if bugun.empty:
        return "Bugün için imsakiye verisi bulunamadı."

    # Akşam (iftar) saatini al
    aksam_str = bugun.iloc[0]["Akşam"]

    # Bugünün iftar datetime'ı
    iftar = pd.to_datetime(
        f"{today.date()} {aksam_str}"
    )

    kalan = iftar - now

    if kalan.total_seconds() < 0:
        return "İftar vakti geçti."

    saat = int(kalan.total_seconds() // 3600)
    dakika = int((kalan.total_seconds() % 3600) // 60)

    return f"İftara {saat} saat {dakika} dakika kaldı."

def Bugun(sehir):
  df = imsakiye(sehir)
  now = datetime.now()
  today = pd.to_datetime(now.date())
  bugun = df[df["Tarih"] == today]
  return bugun

st.header("🌙 Hoş Geldin Ramazan")

sehirler=["Adana", "Adıyaman", "Afyon", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir", "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", "Hakkari", "Hatay", "Isparta", "İçel (Mersin)", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli", "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"
]
sehirsec=st.sidebar.selectbox("Şehirseç", sehirler)

sehirsec = sehirsec.lower()
sehirsec = sehirsec.replace("ç", "c")
sehirsec = sehirsec.replace("ğ", "g")
sehirsec = sehirsec.replace("ı", "i")
sehirsec = sehirsec.replace("ö", "o")
sehirsec = sehirsec.replace("ş", "s")
sehirsec = sehirsec.replace("ü", "u")

st.subheader("İftar Kalan Süre")
st.write(iftara_ne_kadar_kaldi(sehirsec))
st.subheader("Bugünün İmsakiyesi")
st.table(Bugun(sehirsec))
st.table(imsakiye(sehirsec))
gorunen_df = Bugun(sehir).copy()
gorunen_df["Tarih"] = gorunen_df["Tarih"].dt.strftime("%d.%m.%Y")
st.table(gorunen_df)

