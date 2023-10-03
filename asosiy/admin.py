from django.contrib import admin
from .models import *

# admin.site.register(Talaba)
# admin.site.register(Muallif)
# admin.site.register(Kitob)
# admin.site.register(Admin)
# admin.site.register(Record)

@admin.register(Talaba)
class TalabaAdmin(admin.ModelAdmin):
    list_display = ["id","ism","kurs","kitob_soni"]
    list_display_links = ["ism"]
    list_editable = ["kurs","kitob_soni"]
    list_filter = ["kurs"]
    search_fields = ["id","ism","kitob_soni"]
    search_help_text = "Id,ism yoki kitob soni bo'yicha qidiring"
    # list_per_page = 4

@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    list_display = ["id","ism","kitob_soni","jins","tirik"]
    list_display_links = ["id","ism"]
    list_editable = ["kitob_soni","tirik"]
    list_filter = ["tirik"]
    search_fields = ["ism"]
    search_help_text = "Muallif ismi bo'yicha qidiring"

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ["ism","ish_vaqti"]
    list_display_links = ["ism"]
    list_filter = ["ish_vaqti"]
    search_fields = ["ism"]
    search_help_text = "Admin ismi bo'yicha qidiring"

@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    list_display = ["id","nom","janr","sahifa","muallif"]
    list_display_links = ["nom"]
    list_filter = ["janr"]
    list_editable = ["janr"]
    search_fields = ["nom"]
    search_help_text = "Kitob nomi bo'yicha qidiring"

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ["id","olingan_sana","qaytarish_sana","qaytardi"]
    list_filter = ["qaytardi"]
    autocomplete_fields = ["talaba","kitob","admin"]










