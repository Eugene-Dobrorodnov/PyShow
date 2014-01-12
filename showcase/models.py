from django.db import models

class Category(models.Model):
    title = models.CharField(max_length = 160)
    alias = models.CharField(max_length = 160)
    order = models.IntegerField(blank = True, null = True)

    def __unicode__(self):
        return self.title

class SubCategory(models.Model):
    category = models.ForeignKey(Category)
    title    = models.CharField(max_length = 160)
    alias    = models.CharField(max_length = 160)
    order    = models.IntegerField(blank = True, null = True)

    def __unicode__(self):
        return self.title

class Item(models.Model):
    category    = models.ManyToManyField(SubCategory)
    title       = models.CharField(max_length = 250)
    alias       = models.CharField(max_length = 250)
    description = models.TextField()
    price       = models.IntegerField()
    count       = models.IntegerField()
    create_date = models.DateTimeField()

    def __unicode__(self):
        return self.title