from django.db import models

# Create your models here.
class StockData(models.Model):
    high = models.Field()
    last_traded_price = models.Field()
    value_mn = models.Field()
    yesterdays_closing_price = models.Field()
    trade = models.Field()
    volume = models.Field()
    low = models.Field()
    trading_code = models.Field()
    closing_price = models.Field()
    change = models.Field()