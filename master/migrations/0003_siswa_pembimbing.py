# Generated by Django 2.1 on 2019-02-12 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0002_pembimbingsiswa'),
    ]

    operations = [
        migrations.AddField(
            model_name='siswa',
            name='pembimbing',
            field=models.BooleanField(default=False),
        ),
    ]
