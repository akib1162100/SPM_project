# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from StockExchange.models import StockData


class DseScrapingPipeline(object):

    def process_item(self, item, spider):
        StockData.objects.create(
            high=item['high'],
            last_traded_price=item['last_traded_price'],
            value_mn=item['value_mn'],
            yesterdays_closing_price=item['yesterdays_closing_price'],
            trade=item['trade'],
            volume=item['volume'],
            low=item['low'],
            trading_code=item['trading_code'],
            closing_price=item['closing_price'],
            change=item['change']
        )
        return item
