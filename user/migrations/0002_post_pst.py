# Generated by Django 3.0.8 on 2020-08-12 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pst',
            field=models.ImageField(default='default.jpg', upload_to='upload_pics'),
        ),
    ]
