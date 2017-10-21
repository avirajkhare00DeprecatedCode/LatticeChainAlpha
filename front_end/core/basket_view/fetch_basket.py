from service1.models import CryptoBasketUserMapping, CryptoBasket


class FetchBasket():

    def __init__(self, request_data):

        self.request_data = request_data
        self.basket_list = []


    def push_fetch_basket(self):

        for basket in CryptoBasketUserMapping.objects.filter(user_id__username=self.request_data.user.username):

            #print basket.crypto_basket.basket_name

            self.basket_list.append(
                {
                    "basket_name" : basket.crypto_basket.basket_name,
                    "basket_info" : basket.crypto_basket.basket_info
                }
            )

        return self.basket_list