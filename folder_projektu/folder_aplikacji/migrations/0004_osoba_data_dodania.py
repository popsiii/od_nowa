# Generated by Django 5.1.1 on 2024-12-08 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folder_aplikacji', '0003_stanowisko_osoba_plec_osoba_stanowisko'),
    ]

    operations = [
        migrations.AddField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateTimeField(auto_now_add=True, default='2024-12-08'),
            preserve_default=False,
        ),
    ]
