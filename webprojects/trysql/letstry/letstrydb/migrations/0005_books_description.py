# Generated by Django 2.2.4 on 2019-09-21 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letstrydb', '0004_auto_20190921_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='description',
            field=models.CharField(default='', max_length=500),
        ),
    ]