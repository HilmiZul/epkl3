# Generated by Django 2.1 on 2019-03-15 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0007_instansi_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='instansi',
            name='kontak',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AddField(
            model_name='instansi',
            name='pimpinan',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
