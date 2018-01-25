from rest_framework.views import APIView
from rest_framework.response import Response

from front_end.core.token_class.add_user_token import AddERC20Token
from front_end.models import ERC20Address, TokenBasketOrder


class AddUserToken(APIView):
    
    def get(self, request):
        
        return Response(data="No Get")
        
    def post(self, request):
        
        if request.user.is_authenticated():
        
            AddERC20Token(request.user, request.POST['tokenAddress'], request.POST['networkId'])
        
            return Response(200)
            
        else:
            
            return Response(data="not allowed")
            
            
class GetUserTokens(APIView):
    
    def get(self, request):
        
        if request.user.is_authenticated():
            
            tokens = ERC20Address.objects.filter(user_id__username=request.user.username, network_id=request.GET['networkId'])
            token_json = []
            
            for t in tokens:
                token_json.append(t.token_address);
                
            return Response(data=token_json)
        
        else:
            
            return Response(data="not allowed")
            
            
class TokenBasketOrderAPI(APIView):
    
    def post(self, request):
        
        if request.user.is_authenticated():
            
            new_order = TokenBasketOrder()
            
            new_order.user_id = request.user
            new_order.network_id = request.POST['networkId']
            new_order.order_id = request.POST['orderId']
            new_order.seller_token_address_qty = request.POST['sellerTokenAddressQty']
            new_order.ether_asked = request.POST['etherTradeValue']
            new_order.transaction_id = request.POST['transactionId']
            new_order.is_pulled = False
            
            new_order.save()
            
            return Response(200)
            
            
"""
class FetchPreBasketsView(APIView):

    def get(self, request):

        return Response(FetchPreBaskets().return_pre_baskets())

    def post(self, request):

        pass


class FetchSubmitBasket(APIView):

    def get(self, request):

        return Response(data=FetchBasket(request).push_fetch_basket())

    def post(self, request):

        return Response(SubmitBasket(request).submit_basket())


class CreateNewBasketView(APIView):

    def get(self, request):

        pass

    def post(self, request):

        pass

class MarketPlaceView(APIView):

    def get(self, request):

        return render(request, 'html/marketplace.html')

    def post(self, request):

        return Response(data='no post request at this endpoint')

class MarketPlaceBuyView(APIView):

    def get(self, request):

        return render(request, 'html/marketplace_buy.html')

    def post(self, request):

        pass


class MarketPlaceSellView(APIView):

    def get(self, request):

        return render(request, 'html/marketplace_sell.html')

    def post(self, request):

        pass

class MarketPlaceApi(APIView):

    def get(self, request):

        if request.GET['action'] == 'fetch_buy_baskets':

            baskets_data = []

            for basket in BuyBasketExtension.objects.all():

                baskets_data.append(
                    {
                        "basket_id" : basket.basket_id.basket_id,
                        "basket_name" : basket.basket_id.basket_name,
                        "json_data" : basket.basket_id.json_data,
                        "buy_price" : basket.buy_price,
                        "is_negotiable" : basket.is_negotiable,
                        "expiration_date" : basket.expiration_date,
                        "best_ask" : get_bast_value_buy(basket.negotiable_price)
                    }
                )

            return Response(data=baskets_data)

        if request.GET['action'] == 'fetch_sell_baskets':

            baskets_data = []

            for basket in SellBasketExtension.objects.all():

                baskets_data.append(
                    {
                        "basket_id" : basket.basket_id.basket_id,
                        "basket_name" : basket.basket_id.basket_name,
                        "json_data" : basket.basket_id.json_data,
                        "sell_price" : basket.sell_price,
                        "is_negotiable" : basket.is_negotiable,
                        "expiration_date" : basket.expiration_date,
                        "best_ask" : get_bast_value_sell(basket.negotiable_price)
                    }
                )

            return Response(data=baskets_data)


    def post(self, request):

        if request.POST['action'] == "save_bid_price_buy":

            basket = BuyBasketExtension.objects.get(basket_id__basket_id=request.POST['basket_id'])
            if basket.negotiable_price == None:
                basket.negotiable_price = [
                    {
                        "username" : request.user.username,
                        "negotiable_price" : request.POST['bid_price']
                    }
                ]
            else:
                existing_negotiable_array = basket.negotiable_price

                existing_negotiable_array.append(
                    {
                        "username": request.user.username,
                        "negotiable_price": request.POST['bid_price']
                    }
                )

                basket.negotiable_price = existing_negotiable_array

            basket.save()


        elif request.POST['action'] == "save_bid_price_sell":

            basket = SellBasketExtension.objects.get(basket_id__basket_id=request.POST['basket_id'])
            if basket.negotiable_price == None:
                basket.negotiable_price = [
                    {
                        "username" : request.user.username,
                        "negotiable_price" : request.POST['bid_price']
                    }
                ]
            else:
                existing_negotiable_array = basket.negotiable_price

                existing_negotiable_array.append(
                    {
                        "username": request.user.username,
                        "negotiable_price": request.POST['bid_price']
                    }
                )

                basket.negotiable_price = existing_negotiable_array

            basket.save()

        elif request.POST['action'] == "buy":

            BuySellBasketMarketPlace(request, "buy")

        elif request.POST['action'] == "sell":

            BuySellBasketMarketPlace(request, "sell")

        return Response("Oki")

class UserProfileView(APIView):

    def get(self, request):

        return render(request, 'html/profile.html', {
            "user_baskets" : NewCryptoBasket.objects.filter(user_id__username=request.user.username)
        })
        
"""