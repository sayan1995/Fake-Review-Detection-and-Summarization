# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from services.models import Product, Order

admin.site.register(Product)
admin.site.register(Order)
# Register your models here.
