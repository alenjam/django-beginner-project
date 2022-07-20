from django.db import models

# Create your models here.


class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(
        max_length=512,
        default="https://thumbs.dreamstime.com/b/restaurant-blackboard-announcing-reopening-corona-lockdown-cooking-food-business-shutdown-message-coming-soon-183399242.jpg"
    )
