# Dolap Scrapper

## Hakkında
İkinci el ürün pazarı olan dolap.com'a ilgili arama için yeni listeleme yapılıp yapılmadığını kontrol eden bir Python yazılımı.

## Özellikler ve Notlar
- Dockerfile bulundurur.
- Sürekli çalışması gerekmez.
- Mail gönderir.
- Birden fazla arama yapabilir.
- Mesajlar ve yorumlar İngilizcedir.
- Kısa süreli ve kişisel bir kullanım için geliştirdiğim için herhangi bir 'error handling' yazmadım. Bir sıkıntı olursa kendiniz tespit etmeniz gerekecek. (Mail gönderilmez ya da listeleme sayısı okunamaz ise.)
- Birden fazla arama yapma özelliğini sonradan ekledim ve kesinlikle 'düzgün' bir şekilde entegre etmedim. Çalışmasında bir sorun yok ancak tek seferde ikiden fazla arama yapmak isterseniz kodun ne yaptığını anlamanız ve ekleme yapmanız gerekecek. İleride boş zamanım olduğunda düzelteceğim.

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
-  Aradığınız şeyin ne kadar nadir ve hızlı satın alındığına göre sıklığını ayarlayarak cronjob ile kodu çalıştırın: `docker compose -f '/path/to/Dolap Scrapper/docker-compose.yml' up -d`

## Sorun ve Sorular İçin
[GitHub Issues](https://github.com/AlperShal/Dolap-Scrapper/issues)
