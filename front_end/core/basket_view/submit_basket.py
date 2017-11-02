from service1.models import NewCryptoBasket
from django.contrib.auth.models import User
import json

class SubmitBasket():

    def __init__(self, request_data):

        self.request_data = request_data



    def submit_basket(self):

        map_new_basket = NewCryptoBasket()

        map_new_basket.user_id = User.objects.get(username=self.request_data.user.username)
        map_new_basket.basket_id = NewCryptoBasket.objects.all().count() + 1
        map_new_basket.basket_name = self.request_data.POST['basket_name']
        map_new_basket.basket_info = "default discription of basket"
        map_new_basket.price_on_creation = self.request_data.POST['price_on_creation']
        map_new_basket.json_data = self.request_data.POST['basket_json_data']

        map_new_basket.save()

        return "ok"