from django.db import models

# Create your models here.
k = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
)
class Talaba(models.Model):
    ism = models.CharField(max_length=30)
    kurs = models.PositiveIntegerField(choices=k)
    kitob_soni = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.ism

j = (
    ("ayol","ayol"),
    ("erkak","erkak"),
)
class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    jins = models.CharField(max_length=30,choices=j)
    kitob_soni = models.PositiveSmallIntegerField()
    tugilgan_yili = models.DateField(blank=True,null=True)
    tirik = models.BooleanField()

    def __str__(self):
        return self.ism

class Kitob(models.Model):
    nom = models.CharField(max_length=30)
    janr = models.CharField(max_length=30)
    sahifa = models.PositiveIntegerField()
    muallif = models.ForeignKey(Muallif,on_delete=models.CASCADE)

    def __str__(self):
        return self.nom

class Admin(models.Model):
    ism = models.CharField(max_length=30)
    ish_vaqti = models.CharField(max_length=30)

    def __str__(self):
        return self.ism

class Record(models.Model):
    talaba = models.ForeignKey(Talaba,on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob,on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin,on_delete=models.CASCADE)
    olingan_sana = models.DateField(auto_now_add=True)
    qaytarish_sana = models.DateField(blank=True,null=True)
    qaytardi = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.talaba.ism} - {self.kitob.nom}ni {self.olingan_sana}da oldi!"
