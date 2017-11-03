from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, authenticate, logout

from front_end.core.basket_view.fetch_pre_baskets import FetchPreBaskets
from front_end.core.basket_view.fetch_basket import FetchBasket
from front_end.core.basket_view.submit_basket import SubmitBasket

from front_end.core.marketplace_class.send_basket_marketplace import BuySellBasketMarketPlace

from service1.models import NewCryptoBasket, BuyBasketExtension, SellBasketExtension
from front_end.core.util.util1 import get_bast_value_buy, get_bast_value_sell

import requests, json

# Create your views here.

class IndexView(APIView):

    def get(self, request):

        return render(request, 'html/index.html')

    def post(self, request):

        pass


class LoginView(APIView):

    def get(self, request):

        return render(request, 'html/login.html')

    def post(self, request):

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:

            login(request, user)
            return redirect('../dashboard/')

        else:

            return redirect('../login')


class LogoutView(APIView):

    def get(self, request):

        logout(request)
        return redirect('../')

    def post(self, request):

        pass


class DashboardView(APIView):

    def get(self, request):

        #print request.path.split('/')[2]

        if request.user.is_authenticated:

            if request.path.split('/')[2] == 'baskets':

                #some logic before to render template correctly


                return render(request, 'html/dashboard_basket.html')

            return render(request, 'html/dashboard.html')

        else:

            return render(request, 'html/login.html')

    def post(self, request):

        pass


#below is code for many APIs.


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

            for basket in BuyBasketExtension.objects.all().reverse():

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

            for basket in SellBasketExtension.objects.all().reverse():

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