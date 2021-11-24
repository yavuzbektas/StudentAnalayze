from django.contrib import admin

# Register your models here.
from apps.polls.models import OrtaOkulListesi
from apps.polls.models import SoruListesi
from apps.polls.models import Donem
from apps.polls.models import GorevTablosu
from apps.polls.models import Kullanicilar
from apps.polls.models import OgrenciListesi
from apps.polls.models import VeliListesi
from apps.polls.models import SubeListesi
from apps.polls.models import SinifListesi
from apps.polls.models import DersIzlemeSinavlari
from apps.polls.models import AnketListesi
from apps.polls.models import RaporOgrenci
from apps.polls.models import RaporSinif


from apps.polls.models import Question

admin.site.register(OrtaOkulListesi)
admin.site.register(SoruListesi)
admin.site.register(Donem)
admin.site.register(GorevTablosu)
admin.site.register(Kullanicilar)
admin.site.register(OgrenciListesi)
admin.site.register(VeliListesi)
admin.site.register(SubeListesi)
admin.site.register(SinifListesi)
admin.site.register(DersIzlemeSinavlari)
admin.site.register(AnketListesi)
admin.site.register(RaporOgrenci)
admin.site.register(RaporSinif)


admin.site.register(Question)