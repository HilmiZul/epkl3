# Generated by Django 2.2.4 on 2019-09-23 04:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('akun', '0001_initial'),
        ('karya_ilmiah', '0011_auto_20190923_0410'),
    ]

    operations = [
        migrations.AddField(
            model_name='bimbingan',
            name='verified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='akun.AkunPembimbing'),
        ),
    ]
