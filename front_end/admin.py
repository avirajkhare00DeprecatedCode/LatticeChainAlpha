from django.contrib import admin
from models import ERC20Address, TokenBasketOrder, TradableSets
# Register your models here.

admin.site.register(ERC20Address)
admin.site.register(TokenBasketOrder)
admin.site.register(TradableSets)