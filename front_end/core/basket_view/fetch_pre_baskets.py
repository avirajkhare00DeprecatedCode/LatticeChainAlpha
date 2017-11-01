from service1.models import NewCryptoBasket
import json

class FetchPreBaskets():

    def __init__(self):

        self.baskets = []


    def return_pre_baskets(self):

        for basket in NewCryptoBasket.objects.filter(user_id__username='admin'):

            self.baskets.append({
                'basket_id' : basket.basket_id,
                'basket_name' : basket.basket_name,
                'basket_info' : basket.basket_info,
                'amount_allocated' : basket.amount_allocated,
                'basket_json_data' : basket.json_data
            })

        return self.baskets