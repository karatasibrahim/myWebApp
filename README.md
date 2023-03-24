# myWebApp
Django &amp; Tensorflow Project ( Dog Breed Recognition)
![django1](https://user-images.githubusercontent.com/10358635/227653256-ace0b3cf-587a-4989-ae1d-c66fe44096a9.jpg)

Proje için ihtiyacımız olan Anaconda 3.10.4 versiyonu son sürüm
pip install keras
pip install tensorflow
pip install django

Yeni proje oluşturmak için aşağıdaki adımlar izlenir
komut ekranında:

django-admin.exe startproject ProjeAdi

cd .\ProjeAdi\ dosya içerisine gir

python.exe .\manage.py runserver  projeyi derle

dosya içerisinde 

python.exe .\maange.py startapp imgUpload

imgUpload içerisinde new folder => templates

Templates içerisinde home.html ve result.html dosyalarını oluştur

myWebApp klasör içerisinde urls.py dosyası içerisinde url lerimizi ekliyoruz.

views.py içerisine home fonksiyonu ekliyoruz.

ProjeAdi içinde settings.py içerisinde INSTALLED_APPS içerisine 'imgUpload' ekle

https://keras.io/api/applications/ resNet50 kullanıyoruz.
views.py içerisine imageprocess fonksiyonunu yazıyoruz.


PROJEYİ PYTHON ANYWHERE ÜZERİNDE DERLEME

pythonanywhere.com adresine giriş yap

bash console u aç

ls

rm -rf klasörler  makina da ki dosyaları siliyoruz

ssh-keygen

cat .ssh/id_rsa.pub

çıkan keygen makina kimliği bunu github deploy key e yapıştırıyoruz.

github üzerinden ssh kopyala

bash console üzerinde git clone kopyalanan ssh kodu mysite

wsgi config dosyasında düzenleme yapılır. namespace adı olacak şekilde domainname.settings

allowed host hatası için urls.py içerisinde ALLOWED_HOSTS=['*'] yazmamız yeterli

settings.py içerisinde   

'DIRS': [os.path.join(BASE_DIR, "templates"),], eklenir.

https://youtu.be/iUiRwQwS944?list=PLltgmy7jSOUh19FNGr0O_4yeePumnwsmz

    <a href="http://www.youtube.com/watch?feature=player_embedded&v=YOUTUBE_VIDEO_ID_HERE
" target="_blank"><img src="http://img.youtube.com/vi/iUiRwQwS944/10358635/227653256-ace0b3cf-587a-4989-ae1d-c66fe44096a9.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>













