# Generated by Django 2.1 on 2019-03-14 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0006_auto_20190225_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='instansi',
            name='limit',
            field=models.IntegerField(null=True),
        ),
    ]
