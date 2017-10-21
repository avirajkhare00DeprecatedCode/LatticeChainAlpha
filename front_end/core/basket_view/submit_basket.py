from service1.models import CryptoBasketUserMapping, CryptoBasket
from django.contrib.auth.models import User
import json

class SubmitBasket():

    def __init__(self, request_data):

        self.request_data = request_data


    def submit_basket(self):

        map_new_basket = CryptoBasketUserMapping()

        map_new_basket.user_id = User.objects.get(username=self.request_data.user.username)
        map_new_basket.crypto_basket = CryptoBasket.objects.get(basket_id=self.request_data.POST['selected_basket_id'])

        map_new_basket.save()

        return "ok"