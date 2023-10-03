from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


def salom(request):
    return HttpResponse("Salom Dunyo!")


def salomlashish(request):
    content = {
        "ism": "Ali",
        "dostlar": ["Abduvohid", "Abdumalik", "Qobiljon"]
    }
    return render(request, "salom.html", content)


def bosh_sahifa(request):
    return render(request, "bosh_sahifa.html")


def talaba(request, son):
    content = {
        'talaba': Talaba.objects.get(id=son)
    }
    return render(request, "mashq_uchun/talaba.html", content)

def tanlangan_muallif(request, son):
    content = {
        "muallif": Muallif.objects.get(id=son)
    }
    return render(request, "mashq_uchun/tanlangan_muallif.html", content)

def tanlangan_record(request, son):
    content = {
        "record": Record.objects.get(id=son)
    }
    return render(request,  "mashq_uchun/tanlangan_record.html", content)


def tanlangan_kitob(request, son):
    content = {
        "kitob": Kitob.objects.get(id=son)
    }
    return render(request, "mashq_uchun/tanlangan_kitob.html", content)

def talabalar(request):
    if request.method == "POST":
        Talaba.objects.create(
            ism=request.POST.get("ism"),
            kurs=request.POST.get("k"),
            kitob_soni=request.POST.get("k_s")
        )
        return redirect("/talabalar/")
    qidiruv_soz = request.GET.get('ism')
    if qidiruv_soz:
        natija = Talaba.objects.filter(ism__contains=qidiruv_soz)
    else:
        natija = Talaba.objects.all()
    content = {
        "talabalar": natija
    }
    return render(request, "talabalar.html", content)


def talaba_ochir(request, son):
    Talaba.objects.get(id=son).delete()
    return redirect("/talabalar/")

def talaba_edit(request, son):
    if request.method == "POST":
        Talaba.objects.filter(id=son).update(
            kurs=request.POST.get("k"),
            kitob_soni=request.POST.get("k_s")
        )
        return redirect("/talabalar/")
    content = {
        "talaba": Talaba.objects.get(id=son)
    }
    return render(request, "mashq_uchun/talaba_edit.html",content)

def mualliflar(request):
    if request.method == "POST":
        Muallif.objects.create(
            ism=request.POST.get("ism"),
            jins=request.POST.get("j"),
            kitob_soni=request.POST.get("k_s"),
            tugilgan_yili=request.POST.get("t_y"),
            tirik=request.POST.get("t")
        )
        return redirect("/mualliflar/")
    qidiruv_soz = request.GET.get('ismi')
    if qidiruv_soz:
        natija = Muallif.objects.filter(ism__contains=qidiruv_soz)
    else:
        natija = Muallif.objects.all()
    content = {
        "mualliflar": natija
    }
    return render(request, "mualliflar.html", content)


def muallif_ochir(request, son):
    Muallif.objects.get(id=son).delete()
    return redirect("/mualliflar/")

def muallif_edit(request, son):
    if request.method == "POST":
        Muallif.objects.filter(id=son).update(
            kitob_soni=request.POST.get("k_s"),
            tugilgan_yili=request.POST.get("t_y"),
            tirik=request.POST.get("t")
        )
        return redirect("/mualliflar/")
    content = {
        "muallif": Muallif.objects.get(id=son)
    }
    return render(request,"mashq_uchun/muallif.edit.html",content)

def kitoblar(request):
    if request.method == "POST":
            Kitob.objects.create(
                nom=request.POST.get("nom"),
                janr=request.POST.get("j"),
                sahifa=request.POST.get("s"),
                muallif=Muallif.objects.get(id=request.POST.get("m"))
            )
            return redirect("/kitoblar/")
    qidiruv_soz = request.GET.get('nom')
    if qidiruv_soz:
        natija = Kitob.objects.filter(nom__contains=qidiruv_soz)
    else:
        natija = Kitob.objects.all()
    content = {
        "kitoblar": natija,
        "mualliflar": Muallif.objects.all()
    }
    return render(request, "kitoblar.html", content)

def kitob_edit(request, son):
    if request.method == "POST":
        Kitob.objects.filter(id=son).update(
            sahifa=request.POST.get("s")
        )
        return redirect("/kitoblar/")
    content = {
        "kitob": Kitob.objects.get(id=son)
    }
    return render(request,"mashq_uchun/ kitob_edit.html",content)


def adminlar(request):
    if request.method == "POST":
        Admin.objects.create(
            ism=request.POST.get('ism'),
            ish_vaqti=request.POST.get('ish_v')
        )
        return redirect("/adminlar/")
    qidiruv_sozi = request.GET.get('ismi')
    if qidiruv_sozi:
        natija = Admin.objects.filter(ism__contains=qidiruv_sozi)
    else:
        natija = Admin.objects.all()
    content = {
        "adminlar": natija,

    }
    return render(request, "adminlar.html", content)


def recordlar(request):
    if request.method == "POST":
        Record.objects.create(
            talaba=Talaba.objects.get(id=request.POST.get("t")),
            kitob=Kitob.objects.get(id=request.POST.get("k")),
            admin=Admin.objects.get(id=request.POST.get("a")),
            olingan_sana=request.POST.get("olingan_sana"),
            qaytarish_sana=request.POST.get("qaytarish_sana"),
            qaytardi=request.POST.get("q")
        )
        return redirect("/recordlar/")
    qidiruv_sozi = request.GET.get('ismi')
    if qidiruv_sozi:
        natija = Record.objects.filter(talaba__ism__contains=qidiruv_sozi)
    else:
        natija = Record.objects.all()
    content = {
        "recordlar": natija,
        "talabalar": Talaba.objects.all(),
        "adminlar": Admin.objects.all(),
        "kitoblar": Kitob.objects.all(),
    }
    return render(request, "recordlar.html", content)


def record_ochir(request, son):
    Record.objects.get(id=son).delete()
    return redirect('/recordlar/')

def admin_ochir(request, son):
    Admin.objects.get(id=son).delete()
    return redirect('/adminlar/')

def kitob_ochir(request, son):
    Kitob.objects.get(id=son).delete()
    return redirect("/kitoblar/")

#
# def talaba_kitob(request):
#     content = {
#         "kitob_soni": Talaba.objects.filter(Talaba.kitob_soni == 0)
#     }
#     return render(request,"kitob_soni.html",content)


def tirik_muallif(request):
    content = {
        'tirik_muallif': Muallif.objects.filter(tirik=True)
    }
    return render(request, "mashq_uchun/tirik_muallif.html", content)


def a_qatnashgan(request):
    content = {
        'a_qatnashgan': Talaba.objects.filter(ism__contains='a')
    }
    return render(request, "mashq_uchun/a_qatnashgan.html", content)


def kotta_kitob(request):
    content = {
        'kotta_kitob': Kitob.objects.order_by("-sahifa")[:3]
    }
    return render(request, "mashq_uchun/kotta_kitob.html", content)


def muallif_kitobi(request):
    content = {
        "muallif_kitobi": Muallif.objects.order_by("-kitob_soni")[:3]
    }
    return render(request, "mashq_uchun/muallif_kitobi.html", content)


def record_sana(request):
    content = {
        "record_sana": Record.objects.order_by("olingan_sana")[:3]
    }
    return render(request, "mashq_uchun/record_sana.html", content)


def badiiy_kitob(request):
    content = {
        "badiiy_kitob": Kitob.objects.filter(janr="badiiy")
    }
    return render(request, "mashq_uchun/badiiy_kitob.html", content)


def muallif_kitob10(request):
    content = {
        'mualliflar': Muallif.objects.filter(kitob_soni__lt=10)
    }
    return render(request, "mashq_uchun/muallif_kitob10.html", content)


def tirik_muallif(request):
    content = {
        'mualliflar': Muallif.objects.filter(tirik=True)
    }
    return render(request, "mashq_uchun/tirik_muallif.html", content)


def erkak_mualliflar(request):
    content = {
        'mualliflar': Muallif.objects.filter(jins='erkak')
    }
    return render(request, "mashq_uchun/erkak_muallif.html", content)


def bitiruvchi(request):
    content = {
        'bitiruvchilar': Record.objects.filter(talaba__kurs=4)
    }
    return render(request, "mashq_uchun/bitiruvchi.html", content)

