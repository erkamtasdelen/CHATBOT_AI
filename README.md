
---

# CHATBOT_AI

CHATBOT_AI, yapay zeka destekli sohbet asistanı ve görsel üretim özelliklerini barındıran, modüler bir Python projesidir. Projede hem metin tabanlı sohbetler hem de görsel (fotoğraf) üretimi için API entegrasyonları kullanılmıştır. Ana bileşenler arasında Telegram botu, Google’ın Generative AI modeli entegrasyonu ve StarryAI tabanlı görsel üretici modül bulunmaktadır.

---

## İçerik

- [Özellikler](#özellikler)
- [Proje Yapısı](#proje-yapısı)
- [Kurulum ve Gereksinimler](#kurulum-ve-gereksinimler)
- [Konfigürasyon ve API Anahtarları](#konfigürasyon-ve-api-anahtarları)
- [Kullanım Talimatları](#kullanım-talimatları)
  - [Telegram Botu](#telegram-botu)
  - [Sohbet ve AI İşlemleri (ZETA_AI)](#sohbet-ve-ai-işlemleri-zeta_ai)
  - [Fotoğraf Üretimi](#fotoğraf-üretimi)
- [Veri ve Bellek Yönetimi](#veri-ve-bellek-yönetimi)
- [Geliştirme ve Özelleştirme](#geliştirme-ve-özelleştirme)
- [Lisans](#lisans)

---

## Özellikler

- **Telegram Bot Entegrasyonu:** 
  - Telegram üzerinden kullanıcı etkileşimleri.
  - Kullanıcı kayıtlarının ve yetkilendirme işlemlerinin gerçekleştirilmesi.
  - Komutlar: `/start`, `/help`, `/kayit`, `/yetki`, `/yetkiver`, `/sahne`, `/test`, `/foto`.
- **AI Sohbet Asistanı (ZETA_AI):**
  - Google’ın Generative AI (Gemini-2.0 Flash Experiment) modeli kullanılarak gelişmiş metin yanıtları.
  - Konuşma geçmişi, anılar ve bilinç benzeri veri işleme.
  - Kendini “insanlaştırma” ve fiziksel/zeka özelliklerinin saklanması için ek modüller.
- **Fotoğraf Üretimi (PHOTO_GENARATOR):**
  - StarryAI API entegrasyonu ile verilen promptlara göre görsel üretimi.
  - Negatif prompt parametreleri sayesinde düşük kaliteli ya da istenmeyen detayları engelleme.

---

## Proje Yapısı

```
CHATBOT_AI/
├── Brain/
│   ├── Chat_Pass.json       # Sohbet geçmişi ve chat verilerinin saklandığı JSON dosyası
│   ├── PERSONS.txt          # Telegram kullanıcı kayıtlarının tutulduğu dosya
│   ├── PrePromt_General.json# Genel bilgi ve AI’nın davranış biçimini etkileyen ön ayarlar
│   ├── kiyafet_ve_lokasyon.txt  # Fiziksel özellikler & mekan algısı verileri
│   ├── ozfarkindalik.txt    # AI’nın “öz bilinç” bilgileri, kişisel anılar vb.
│   └── MEMOS/               # Uzun süreli hafıza ve anı kayıtlarının tutulduğu klasör
├── GOODEXAMPLES/           # Örnek kullanım veya referans kod parçacıkları (isteğe bağlı)
├── PreLearn/               # Önceden öğrenilmiş veriler, metin dosyaları ve eğitim materyalleri
├── __pycache__/            # Python derlenmiş dosyaları (otomatik oluşturulan klasör)
├── PHOTO_GENARATOR.py      # Görsel üretim API’si ile etkileşim sağlayan modül (IMAGE_CREATE sınıfı)
├── TELEGRAM.py             # Telegram botu arayüzü; komutlar, mesaj işleme ve kullanıcı yönetimi
├── ZETA AI.rar            # (Opsiyonel) Ek kaynaklar, modeller veya veri setlerini içeren arşiv
└── ZETA_AI.py             # Ana yapay zeka modülü; sohbet yönetimi, bellek, anı işleme ve AI yanıt üretimi
```

---

## Kurulum ve Gereksinimler

1. **Python Sürümü:** Proje, Python 3.x ile uyumludur.
2. **Gerekli Kütüphaneler:**
   - `requests`
   - `googleapiclient`
   - `google.generativeai`
   - `python-telegram-bot`
   - Diğer yardımcı modüller: `json`, `uuid`, `datetime`, `os`, `time`, `threading`
   
   Gerekli kütüphaneler için bir `requirements.txt` dosyası oluşturabilir ve aşağıdaki komutla yükleyebilirsiniz:
   ```bash
   pip install -r requirements.txt
   ```
   (Eğer böyle bir dosya yoksa, proje dosyalarında kullanılan kütüphaneleri manuel olarak yükleyin.)

---

## Konfigürasyon ve API Anahtarları

- **Google Generative AI API Anahtarı:**  
  ZETA_AI modülünde AI sınıfı oluşturulurken Google API anahtarı gerekmektedir. `ZETA_AI.py` içerisindeki `AI` sınıfının yapıcı metoduna verilen API anahtarını (örneğin `"AIzaSyDIjkfs-__snf72Ki4YjiGueDX-vRLAQPY"`) kendi API anahtarınızla değiştirin.

- **StarryAI API Anahtarı:**  
  `PHOTO_GENARATOR.py` dosyasında, `IMAGE_CREATE` sınıfı API anahtarını parametre olarak alır. Kendi StarryAI API anahtarınızı kullanarak bu değeri güncelleyin.

- **Telegram Bot Token:**  
  `TELEGRAM.py` dosyasında BotFather’dan aldığınız tokeni ilgili yere ekleyin (örneğin `"7611812339:AAEkyEyCP2_-DZgopfPdNOY3e8xAh8thMno"`).

- **Sahip ve Yapay Zeka İsimleri:**  
  `ZETA_AI.py` dosyasında, `YAPAY_ZEKANIN_İSMİ`, `SAHİP_İSMİ` ve diğer karakter tanımlamaları düzenlenebilir. Bu değerler, AI’nın kişiliği ve yanıt üretimindeki bağlamı etkiler.

---

## Kullanım Talimatları

### Telegram Botu

- **Başlatma:**  
  `TELEGRAM.py` dosyasını çalıştırarak Telegram botunuz aktif hale gelir. Bot, kullanıcı komutları aracılığıyla çeşitli işlevleri yerine getirir.
  
- **Temel Komutlar:**
  - `/start`: Botu başlatır ve karşılama mesajı gönderir.
  - `/help`: Kullanılabilir komutların listesini gösterir.
  - `/kayit`: Kullanıcı kaydını başlatır (AI ile etkileşim sırasında ilgili test alanı çalıştırılır).
  - `/yetki` ve `/yetkiver`: Özellikle sahibi (örneğin belirli chat ID’ye sahip kullanıcı) tarafından yetkilendirme işlemleri için kullanılır.
  - `/sahne`: AI’nın mevcut “sahne” veya olay algısını döndürür.
  - `/test`: AI’nın test fonksiyonlarını çalıştırır.
  - `/foto`: Görsel üretim modülünü tetikleyerek, AI’nın fiziksel ve mekan algısını görsel prompta çevirir ve görüntü URL’si döner.

- **Kullanıcı Kayıtları:**  
  `Brain/PERSONS.txt` dosyası, yetkilendirilmiş kullanıcıların kayıtlarını tutar. Yeni kullanıcılar eklenirken bu dosya güncellenir.

### Sohbet ve AI İşlemleri (ZETA_AI)

- **AI Sınıfı:**  
  `ZETA_AI.py` dosyası, AI davranışını kontrol eden ana sınıftır. 
  - **Özellikler:**
    - **Sohbet Geçmişi ve Bellek Yönetimi:** Sohbet geçmişi `Brain/Chat_Pass.json` dosyasında saklanır. AI, geçmiş konuşmaları kullanarak bağlamsal yanıtlar üretir.
    - **Kendini Güncelleme:** AI; fiziksel özellikler, zeka seviyesi, mekan algısı ve duygusal durum gibi bilgileri düzenli olarak günceller.
    - **Kendi Kendine Soru Sorma:** `selfask` metodu ile AI, verilen metinlere göre kendi kendine analiz yapar ve yanıt üretir.
    - **Anı ve Hafıza İşlemleri:** `chatsave`, `Anilar`, `TESTAREA` gibi metotlarla uzun süreli hafıza oluşturma ve verileri konsolide etme işlemleri yapılır.
    - **İletişim Kararı:** `questionitself` metodu, AI’nın sahibi ile iletişim kurma gerekliliğini değerlendirir.
    
- **Kullanım:**  
  ZETA_AI sınıfı, diğer modüller (örneğin Telegram botu) tarafından çağrılarak sohbet işlemleri gerçekleştirilir. AI’ya gönderilen promptlar, güncel saat, chat geçmişi ve diğer bağlamsal verilerle zenginleştirilir.

### Fotoğraf Üretimi

- **IMAGE_CREATE Sınıfı:**  
  `PHOTO_GENARATOR.py` dosyasında yer alan bu sınıf, StarryAI API’ı kullanarak görsel üretimi yapar.
  - **CREATE_IMAGE Metodu:**  
    Belirtilen prompt (ve negatif prompt) ile API’ye istek gönderir. Oluşturulan görselin durumunu periyodik sorgularla takip eder ve tamamlandığında görsel URL’sini döndürür.
  - **Negatif Prompt:**  
    Varsayılan negatif prompt, istenmeyen görsel bozuklukları (blurry, distorted, extra limbs vb.) engellemek üzere tanımlanmıştır.

- **Entegrasyon:**  
  `ZETA_AI.py` içindeki `Photo` metodu, fiziksel özellikler, mekan algısı ve sohbet geçmişini kullanarak detaylı bir İngilizce görsel tanım promptu oluşturur ve IMAGE_CREATE modülü üzerinden görsel üretimi sağlar.

---

## Veri ve Bellek Yönetimi

- **Sohbet Geçmişi:**  
  Tüm sohbetler JSON formatında `Brain/Chat_Pass.json` dosyasına kaydedilir. Bu geçmiş, AI’nın bağlamsal yanıt üretiminde kullanılır.
- **Uzun Süreli Hafıza:**  
  AI, `Brain/MEMOS` klasöründeki dosyalar aracılığıyla sürekli hafıza (anı) güncellemesi yapar. `TESTAREA` ve `TESTAREA2` metotları, bu hafızayı derinleştirmek için kullanılır.
- **Fiziksel ve Zeka Özellikleri:**  
  AI’nın fiziksel özellikleri `Brain/fiziksel.txt`, zeka özellikleri ise `Brain/zeka.txt` dosyalarında saklanır. İlk başlatma sırasında, AI kendini “insanlaştırma” amacıyla gerekli bilgileri oluşturur.
- **Mekan Algısı:**  
  `Brain/kiyafet_ve_lokasyon.txt` dosyası, AI’nın çevre algısını ve konum bilgilerini içerir. Bu veriler, görsel tanım oluşturulurken kullanılır.

---

## Geliştirme ve Özelleştirme

- **Ön Eğitim Verileri:**  
  `PreLearn/` klasöründeki dosyalar, AI’nın önceden öğrenmiş olabileceği ek bilgiler içerir. `prelearn` metodu bu verileri alarak AI’nın hafızasına entegre edebilir.
- **Kod Düzenlemeleri:**  
  Projede yer alan API anahtarları, karakter isimleri ve diğer kişiselleştirilebilir değişkenler kullanıcı tarafından kolayca düzenlenebilir.
- **Genişletilebilirlik:**  
  Mevcut yapıyı, farklı AI modelleri, ek komutlar veya görsel işleme özellikleri ekleyerek genişletebilirsiniz.

---


---

## Son Notlar

CHATBOT_AI, farklı API entegrasyonlarını ve gelişmiş bellek yönetimini bir araya getirerek hem metin hem de görsel üretimi yapan yenilikçi bir asistan oluşturmayı hedefler. Projeyi kullanmadan önce ilgili API anahtarlarınızı ve konfigürasyon ayarlarınızı güncellemeyi unutmayın.

Herhangi bir sorunuz ya da geliştirme öneriniz için lütfen iletişime geçin.

---

