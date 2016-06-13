from __future__ import unicode_literals
from django.db import models
from django.utils.text import slugify


class InfoPage(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __unicode__(self):
        return self.name


class Item(models.Model):
    page = models.ForeignKey(InfoPage)
    headline = models.CharField(max_length=40)
    element_id = models.CharField(max_length=40)
    order = models.IntegerField()
    text = models.CharField(max_length=4000)

    def save(self, *args, **kwargs):
        self.element_id = slugify(self.headline)
        super(Item, self).save(*args, **kwargs)

    def table_class(self):

        new_self = self.text.replace('<table border="1" cellpadding="1" cellspacing="1" style="width:500px">',
                                     '<table class="table table-striped" style="text-align: center">')
        new_self = new_self.replace('<p>', '<p style="text-align: justify">')
        return new_self

    def __unicode__(self):
        return str(self.order)


class SiteSetting(models.Model):

    site_name = models.CharField(max_length=40)
    full_name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    venue = models.CharField(max_length=60, blank=True)
    location = models.CharField(max_length=60)

    abstract_deadline = models.DateField()
    acceptance_deadline = models.DateField()
    papers_deadline = models.DateField()
    registration_deadline = models.DateField()

    full_price_registration = models.IntegerField(default=0)
    student_price_registration = models.IntegerField(default=0)
    one_day_registration = models.IntegerField(default=0, help_text="Leave at 0 if no one day registration available.")
