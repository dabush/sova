# Generated by Django 2.1.4 on 2019-01-04 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('texts', '0007_auto_20190104_2036'),
    ]

    operations = [
        migrations.AddField(
            model_name='text',
            name='text_featured',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]