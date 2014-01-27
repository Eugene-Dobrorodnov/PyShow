from django.db import models
from django.utils import timezone

def default_date():
    return timezone.now()

class Category(models.Model):
    title = models.CharField(max_length = 160, unique = True)
    slug  = models.SlugField(unique = True, max_length = 160)
    order = models.IntegerField(blank = True, null = True)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name        = u'Category'
        verbose_name_plural = u'Categorys'
        ordering            = [u'title']

class SubCategory(models.Model):
    category = models.ForeignKey(Category)
    slug     = models.SlugField(unique = True, max_length = 160)
    title    = models.CharField(max_length = 160, unique = True)
    order    = models.IntegerField(blank = True, null = True)

    def __unicode__(self):
        return self.title

class Item(models.Model):
    category    = models.ForeignKey(SubCategory)
    title       = models.CharField(max_length = 250, unique = True)
    slug        = models.SlugField(unique = True, max_length = 250)
    description = models.TextField()
    price       = models.DecimalField(max_digits = 22, decimal_places = 2)
    count       = models.IntegerField()
    create_date = models.DateTimeField()

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    item        = models.ForeignKey(Item)
    body        = models.TextField()
    create_date = models.DateTimeField(default = default_date())