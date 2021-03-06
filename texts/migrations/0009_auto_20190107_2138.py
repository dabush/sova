# Generated by Django 2.1.4 on 2019-01-07 21:38

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('texts', '0008_text_text_featured'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='theme',
            options={'ordering': ('theme_name',)},
        ),
        migrations.AddField(
            model_name='author',
            name='author_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2019, 1, 7, 21, 38, 21, 315336, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='author_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='owner',
            name='owner_created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2019, 1, 7, 21, 38, 26, 906645, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='owner',
            name='owner_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='text',
            name='text_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='theme',
            name='theme_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theme',
            name='theme_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
