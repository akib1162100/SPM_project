# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from StockExchange.models import StockData


class DSEItem(DjangoItem):
    django_model = StockData
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
