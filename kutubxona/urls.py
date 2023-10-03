
from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('salom/', salom),
    path('salomlash/', salomlashish),
    path('', bosh_sahifa),
    path('talaba/<int:son>/', talaba),
    path('kitob/<int:son>/', tanlangan_kitob),
    path('muallif/<int:son>/', tanlangan_muallif),
    path('record/<int:son>/', tanlangan_record),
    path('talaba_ochir/<int:son>/', talaba_ochir),
    path('admin_ochir/<int:son>/', admin_ochir),
    path('kitob_ochir/<int:son>/', kitob_ochir),
    path('talabalar/', talabalar),
    path('talaba_edit/<int:son>/', talaba_edit),
    path('muallif_edit/<int:son>/', muallif_edit),
    path('mualliflar/', mualliflar),
    path('muallif_ochir/<int:son>/', muallif_ochir),
    path('kitob_edit/<int:son>/', kitob_edit),
    path('kitoblar/', kitoblar),
    path('adminlar/', adminlar),
    path('recordlar/', recordlar),
    path('record_ochir/<int:son>/', record_ochir),
    path('tirik_muallif/', tirik_muallif),
    path('a_qatnashgan/', a_qatnashgan),
    path('kotta_kitob/', kotta_kitob),
    path('muallif_kitobi/', muallif_kitobi),
    path('record_sana/', record_sana),
    path('badiiy_kitob/', badiiy_kitob),
    path('tirik_muallif/', tirik_muallif),
    path('erkak_mualliflar/', erkak_mualliflar),
    path('bitiruvchi/', bitiruvchi),
    # path('talaba_kitob/', talaba_kitob),
]

