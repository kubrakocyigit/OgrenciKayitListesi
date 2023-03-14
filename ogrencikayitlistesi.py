# öğrenci listesi
ogrenciler = []

# öğrenci ekleme fonksiyonu
def ogrenci_ekle(ad, soyad):
    ogrenci = ad + " " + soyad
    ogrenciler.append(ogrenci)
    print(f"{ogrenci} öğrenci listesine eklendi.")

# öğrenci silme fonksiyonu
def ogrenci_sil(ad, soyad):
    ogrenci = ad + " " + soyad
    if ogrenci in ogrenciler:
        ogrenciler.remove(ogrenci)
        print(f"{ogrenci} öğrenci listesinden silindi.")
    else:
        print(f"{ogrenci} öğrenci listesinde bulunamadı.")

def ogrencileri_toplu_ekle(adlar, soyadlar):
    for i in range(len(adlar)):
        ogrenci_ekle(adlar[i], soyadlar[i])
# öğrenci listeleme fonksiyonu
def ogrenci_listele():
    print("Öğrenci listesi:")
    for i, ogrenci in enumerate(ogrenciler):
        print(f"{i} - {ogrenci}")

# öğrenci numarası öğrenme fonksiyonu
def ogrenci_no_bul(ad, soyad):
    ogrenci = ad + " " + soyad
    if ogrenci in ogrenciler:
        no = ogrenciler.index(ogrenci)
        print(f"{ogrenci} öğrencisinin numarası: {no}")
    else:
        print(f"{ogrenci} öğrencisi listede bulunamadı.")

# birden fazla öğrenci silme fonksiyonu
def ogrencileri_toplu_sil(adlar, soyadlar):
    for ad, soyad in zip(adlar, soyadlar):
        ogrenci_sil(ad, soyad)

# kullanıcı dostu menü
while True:
    print("""
    Öğrenci Kayıt Sistemi

    1 - Öğrenci Ekle
    2 - Öğrenci Sil
    3 - Birden Fazla Öğrenci Ekle
    4 - Öğrencileri Listele
    5 - Öğrenci Numarası Bul
    6 - Birden Fazla Öğrenci Sil
    0 - Çıkış

    """)

    secim = input("Yapmak istediğiniz işlemi seçin: ")
    if secim == "1":
        ad = input("Öğrenci adı: ")
        soyad = input("Öğrenci soyadı: ")
        ogrenci_ekle(ad, soyad)
    elif secim == "2":
        ad = input("Öğrenci adı: ")
        soyad = input("Öğrenci soyadı: ")
        ogrenci_sil(ad, soyad)
    elif secim == "3":
        adlar = input("Eklemek istediğiniz öğrencilerin adlarını aralarında boşluk bırakarak yazın: ")
        soyadlar = input("Eklemek istediğiniz öğrencilerin soyadlarını aralarında boşluk bırakarak yazın: ")
        adlar = adlar.split()
        soyadlar = soyadlar.split()
        ogrencileri_toplu_ekle(adlar, soyadlar)
    elif secim == "4":
        ogrenci_listele()
    elif secim == "5":
        ad = input("Öğrenci adı: ")
        soyad = input("Öğrenci soyadı: ")
        ogrenci_no_bul(ad, soyad)
    elif secim == "6":
        adlar = input("Silmek istediğiniz öğrencilerin adlarını aralarında boşluk bırakarak yazın: ")
        soyadlar = input("Silmek istediğiniz öğrencilerin soyadlarını aralarında boşluk bırakarak yazın: ")
        adlar = adlar.split()
        soyadlar = soyadlar.split()
        ogrencileri_toplu_sil(adlar, soyadlar)
    elif secim == "0":
        print("Programdan çıkılıyor...")
        break
    else:
        print("Geçersiz seçim. Lütfen tekrar deneyin.")
    
    

