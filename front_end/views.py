from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, authenticate, logout

from front_end.core.basket_view.fetch_pre_baskets import FetchPreBaskets
from front_end.core.basket_view.fetch_basket import FetchBasket
from front_end.core.basket_view.submit_basket import SubmitBasket

from service1.models import NewCryptoBasket

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

class UserProfileView(APIView):

    def get(self, request):

        return render(request, 'html/profile.html', {
            "user_baskets" : NewCryptoBasket.objects.filter(user_id__username=request.user.username)
        })