# Generated by Django 2.1.4 on 2018-12-04 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20181204_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='posts/static/posts/postimg'),
        ),
    ]
