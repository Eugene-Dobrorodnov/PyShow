from django.db import models
from showcase.models import Item
from django.contrib.auth.models import User

class Oreders(models.Model):
    item_id     = models.ForeignKey(Item)
    user_id     = models.ForeignKey(User)
    create_date = models.DateTimeField()