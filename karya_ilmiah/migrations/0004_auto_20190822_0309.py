# Generated by Django 2.2.4 on 2019-08-22 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karya_ilmiah', '0003_bimbingan_catatan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bimbingan',
            name='catatan',
            field=models.TextField(default=None, null=True),
        ),
    ]
