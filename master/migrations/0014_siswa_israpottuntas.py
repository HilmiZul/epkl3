# Generated by Django 2.2.12 on 2021-04-27 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0013_auto_20210427_0918'),
    ]

    operations = [
        migrations.AddField(
            model_name='siswa',
            name='isRapotTuntas',
            field=models.BooleanField(default=True, null=True),
        ),
    ]
