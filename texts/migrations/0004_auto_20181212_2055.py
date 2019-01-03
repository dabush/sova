# Generated by Django 2.1.4 on 2018-12-12 20:55

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('texts', '0003_auto_20181211_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='text_url',
            field=models.URLField(default='www.google.com', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='author',
            name='author_bio',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='text',
            name='text_original',
            field=tinymce.models.HTMLField(verbose_name='Original'),
        ),
        migrations.AlterField(
            model_name='text',
            name='text_translation',
            field=tinymce.models.HTMLField(verbose_name='Translation'),
        ),
    ]
