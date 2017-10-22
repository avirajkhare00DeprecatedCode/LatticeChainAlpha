from django.contrib import admin

# Register your models here.
from service1.models import UserDetails, CryptoBasket, CryptoCoins, ERC20Tokens, AllocationObject, NewCryptoBasket, CryptoCoinsNew

admin.site.register(UserDetails)
admin.site.register(CryptoBasket)
admin.site.register(CryptoCoins)
admin.site.register(ERC20Tokens)
admin.site.register(AllocationObject)
admin.site.register(NewCryptoBasket)
admin.site.register(CryptoCoinsNew)