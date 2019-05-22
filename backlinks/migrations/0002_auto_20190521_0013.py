# Generated by Django 2.2.1 on 2019-05-20 21:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backlinks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='backlinks',
            name='source',
            field=models.URLField(default=django.utils.timezone.now, max_length=100, verbose_name='Kaynak'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='backlinks',
            name='end_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Bitiş Tarihi'),
        ),
        migrations.AlterField(
            model_name='backlinks',
            name='link',
            field=models.URLField(max_length=100, verbose_name='Link'),
        ),
    ]
