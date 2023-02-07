# Dolap Scrapper

## Hakkında
İkinci el ürün pazarı olan dolap.com'a ilgili arama için yeni listeleme yapılıp yapılmadığını kontrol eden bir Python yazılımı.

## Özellikler ve Notlar
- Dockerfile bulundurur.
- Sürekli çalışması gerekmez.
- Mail gönderir.
- Mesajlar ve yorumlar İngilizcedir.
- Kısa süreli ve kişisel bir kullanım için geliştirdiğim için herhangi bir 'error handling' yazmadım. Bir sıkıntı olursa kendiniz tespit etmeniz gerekecek. (Mail gönderilmez ya da listeleme sayısı okunamaz ise.)

## Gereksinimler
- Python
- Mail Sunucusu

Opsiyonel:
- Docker
- Docker Compose

## Kullanım
### Sunucuda
`main.py`'deki ilgili değişkenleri doldurun (Mail bilgileri, Dolap linki vs.) ve sunucunuza yükleyin. Aradığınız şeyin ne kadar nadir ve hızlı satın alındığına göre sıklığını ayarlayarak cronjob ile çalıştırın. (Ben saat 06.00'dan 01.00'a bir kaç kez çalıştırıyorum.)

### Docker Konteynerinde
- `main.py`'deki ilgili değişkenleri doldurun (Mail bilgileri, Dolap linki vs.) ve sunucunuza yükleyin.
- Dosyaların olduğu dizinde `docker build -t dolap-scrapper .` komutu ile konteyneri oluşturun.
- `docker run -it --rm --name py dolap-scrapper:latest` komutuyla kodun çalışıp çalışmadığını kontrol edin.
- Docker Compose kullanarak konteynerdeki güncellenen dosyaların ana makineye de kayıt edilmesini sağlayın (Volume Bind) (Sunucunuzda dosyaların olduğu konumu yml'de düzenlemeyi unutmayın.):
```
services:
  dolap-scrapper:
    image: dolap-scrapper:latest
    container_name: dolap-scrapper
    volumes:
      - /path/to/Dolap-Scrapper:/usr/src/app
```
-  Aradığınız şeyin ne kadar nadir ve hızlı satın alındığına göre sıklığını ayarlayarak cronjob ile kodu çalıştırın: `docker compose up -d dolap-scrapper`

## Sorun ve Sorular İçin
[GitHub Issues](https://github.com/AlperShal/Dolap-Scrapper/issues)