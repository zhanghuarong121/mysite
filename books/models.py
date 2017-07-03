# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=100)
    authors=models.CharField(max_length=30)
    publisher=models.CharField(max_length=40)
    publication_date=models.DateField()

