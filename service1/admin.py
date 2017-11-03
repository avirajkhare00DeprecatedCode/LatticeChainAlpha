from django.contrib import admin

# Register your models here.
from service1.models import UserDetails, NewCryptoBasket, CryptoCoinsNew, BuyBasketExtension, SellBasketExtension

admin.site.register(UserDetails)
admin.site.register(BuyBasketExtension)
admin.site.register(NewCryptoBasket)
admin.site.register(SellBasketExtension)