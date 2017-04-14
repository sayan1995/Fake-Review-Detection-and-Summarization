# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
import uuid

class Product(models.Model):

    def __str__(self):
        return self.name

class Order(models.Model):


    def __str__(self):
        return self.id
