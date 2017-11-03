from service1.models import NewCryptoBasket, BuyBasketExtension, SellBasketExtension

class BuySellBasketMarketPlace:

    def __init__(self, request_data, action):

        if action == "buy":

            basket = BuyBasketExtension()
            basket.basket_id = NewCryptoBasket.objects.get(basket_id=request_data.POST['basket_id'])
            basket.buy_price = request_data.POST['buy_price']
            basket.expiration_date = request_data.POST['expiration_date']
            basket.is_negotiable = request_data.POST['is_negotiable']

            basket.save()

        elif action == "sell":

            basket = SellBasketExtension()
            basket.basket_id = NewCryptoBasket.objects.get(basket_id=request_data.POST['basket_id'])
            basket.sell_price = request_data.POST['sell_price']
            basket.expiration_date = request_data.POST['expiration_date']
            basket.is_negotiable = request_data.POST['is_negotiable']

            basket.save()