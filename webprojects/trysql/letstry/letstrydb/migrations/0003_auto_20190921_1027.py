# Generated by Django 2.2.4 on 2019-09-21 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letstrydb', '0002_auto_20190921_0634'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='availability',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='books',
            name='category',
            field=models.CharField(default='Others', max_length=50),
        ),
        migrations.AddField(
            model_name='books',
            name='isbn',
            field=models.CharField(default='1E1E', max_length=50),
        ),
        migrations.AddField(
            model_name='books',
            name='thumbnail',
            field=models.CharField(default='https://SOME STRING', max_length=50),
        ),
    ]
