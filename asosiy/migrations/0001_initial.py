# Generated by Django 4.2.2 on 2023-09-12 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('ish_vaqti', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Kitob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30)),
                ('janr', models.CharField(max_length=30)),
                ('sahifa', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Muallif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('jins', models.CharField(choices=[('ayol', 'ayol'), ('erkak', 'erkak')], max_length=30)),
                ('kitob_soni', models.PositiveSmallIntegerField()),
                ('tugilgan_yili', models.DateField(blank=True, null=True)),
                ('tirik', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Talaba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=30)),
                ('kurs', models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)])),
                ('kitob_soni', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('olingan_sana', models.DateField(auto_now_add=True)),
                ('qaytarish_sana', models.DateField(blank=True, null=True)),
                ('qaytardi', models.BooleanField(default=False)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.admin')),
                ('kitob', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.kitob')),
                ('talaba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.talaba')),
            ],
        ),
        migrations.AddField(
            model_name='kitob',
            name='muallif',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.muallif'),
        ),
    ]
