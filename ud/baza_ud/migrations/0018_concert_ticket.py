# Generated by Django 3.0.1 on 2019-12-24 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baza_ud', '0017_remove_concert_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='ticket',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Ссылка на покупку билета'),
        ),
    ]
