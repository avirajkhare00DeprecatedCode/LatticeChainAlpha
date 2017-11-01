from service1.models import NewCryptoBasket


class FetchBasket():

    def __init__(self, request_data):

        self.request_data = request_data
        self.basket_list = []


    def push_fetch_basket(self):

        for basket in NewCryptoBasket.objects.filter(user_id__username=self.request_data.user.username):

            #print basket.crypto_basket.basket_name

            self.basket_list.append(
                {
                    "basket_name" : basket.basket_name,
                    "basket_info" : basket.basket_info,
                    "amount_allocated" : basket.amount_allocated
                }
            )

        return self.basket_list