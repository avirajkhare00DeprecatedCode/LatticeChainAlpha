from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, authenticate, logout

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

        if request.user.is_authenticated:

            return render(request, 'html/dashboard.html')

        else:

            return redirect('../login/')

    def post(self, request):

        pass


#Put all api classes inside api_calls file