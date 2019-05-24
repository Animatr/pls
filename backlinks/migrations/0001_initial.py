# Generated by Django 2.2.1 on 2019-05-24 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Backlinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(max_length=100, verbose_name='Link')),
                ('keyword', models.CharField(max_length=100, verbose_name='Anahtar Kelime')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Eklenme Tarihi')),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Bitiş Tarihi')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Ek Bilgi')),
                ('source', models.URLField(max_length=100, verbose_name='Kaynak')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
            options={
                'verbose_name': 'Backlink',
                'verbose_name_plural': 'Backlinkler',
            },
        ),
    ]
