# Generated by Django 2.2.4 on 2019-09-21 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letstrydb', '0003_auto_20190921_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='thumbnail',
            field=models.CharField(default='https://SOME STRING', max_length=150),
        ),
    ]