from django.contrib import admin
# Register your models here.
from .models import OrtaOkulListesi
from .models import SoruListesi
from .models import Donem
from .models import GorevTablosu
from .models import Kullanicilar
from .models import OgrenciListesi
from .models import VeliListesi
from .models import SubeListesi
from .models import SinifListesi
from .models import DersIzlemeSinavlari
from .models import AnketListesi
from .models import RaporOgrenci
from .models import RaporSinif


from .models import Question

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