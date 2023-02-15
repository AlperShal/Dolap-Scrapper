# Dolap Scrapper

## Hakkında
İkinci el ürün pazarı dolap.com'a ilgili arama için yeni listeleme yapılıp yapılmadığını kontrol eden bir Python yazılımı.

## Özellikler ve Notlar
- Birden fazla arama yapabilir.
- Mail gönderir.
- Sürekli çalışması gerekmez.
- Mesajlar ve yorumlar İngilizcedir.
- Dockerfile bulundurur.
- Kısa süreli ve kişisel bir kullanım için geliştirdiğim için herhangi bir 'error handling' yazmadım. Bir sıkıntı olursa kendiniz tespit etmeniz gerekecek. (Mail gönderilmez ya da listeleme sayısı okunamaz ise.)

## Gereksinimler
- Python
- Mail Sunucusu

Opsiyonel:
- Docker
- Docker Compose

## Kullanım
### Sunucuda
`main.py`'deki ilgili değişkenleri doldurun (Mail bilgileri, aranan ürün vs.) ve sunucunuza yükleyin. Aradığınız şeyin ne kadar nadir ve hızlı satın alındığına göre sıklığını ayarlayarak cronjob ile çalıştırın. (Ben saat 06.00'dan 01.00'a bir kaç kez çalıştırıyorum.)

### Docker Konteynerinde
- `main.py`'deki ilgili değişkenleri doldurun (Mail bilgileri, aranan ürün vs.) ve sunucunuza yükleyin.
- Dosyaların olduğu dizinde `docker build -t dolap-scrapper .` komutu ile konteyneri oluşturun.
- `docker run -it --rm --name py dolap-scrapper:latest` komutuyla kodun çalışıp çalışmadığını kontrol edin.
-  Aradığınız şeyin ne kadar nadir ve hızlı satın alındığına göre sıklığını ayarlayarak cronjob ile kodu çalıştırın: `docker compose -f '/path/to/dolap-scrapper/docker-compose.yml' up -d`

## Sorun ve Sorular İçin
[GitHub Issues](https://github.com/AlperShal/dolap-scrapper/issues)
