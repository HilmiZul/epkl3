# Generated by Django 2.2.12 on 2021-04-08 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_kompetensidasar'),
    ]

    operations = [
        migrations.AddField(
            model_name='siswa',
            name='jk',
            field=models.CharField(choices=[('L', 'L'), ('P', 'P')], max_length=1, null=True),
        ),
    ]
