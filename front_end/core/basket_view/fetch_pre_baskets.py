from service1.models import CryptoBasket
import json

class FetchPreBaskets():

    def __init__(self):

        self.baskets = []


    def return_pre_baskets(self):

        for basket in CryptoBasket.objects.filter(user_id__username='admin'):

            self.baskets.append({
                'basket_id' : basket.basket_id,
                'basket_name' : basket.basket_name,
                'basket_info' : basket.basket_info
            })

        return self.baskets