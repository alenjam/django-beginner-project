# Generated by Django 4.0.6 on 2022-07-19 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://pluspack.com/wp-content/uploads/2018/09/placeholder-picture.jpg', max_length=512),
        ),
    ]
