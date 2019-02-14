# Generated by Django 2.1 on 2019-02-12 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('master', '0001_initial'),
        ('akun', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AkunSiswa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.Siswa')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]