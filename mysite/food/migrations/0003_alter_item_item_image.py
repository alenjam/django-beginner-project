# Generated by Django 4.0.6 on 2022-07-19 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://thumbs.dreamstime.com/b/restaurant-blackboard-announcing-reopening-corona-lockdown-cooking-food-business-shutdown-message-coming-soon-183399242.jpg', max_length=512),
        ),
    ]
