from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, authenticate, logout

from front_end.core.basket_view.fetch_pre_baskets import FetchPreBaskets

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

        return FetchPreBaskets.return_pre_baskets()

    def post(self, request):

        pass