# Generated by Django 2.1 on 2019-09-17 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_auto_20190911_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='detail',
            field=models.TextField(blank=True, default=' ', max_length=350, verbose_name='Поробное описание'),
        ),
    ]
