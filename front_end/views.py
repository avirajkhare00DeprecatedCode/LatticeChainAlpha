from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import logout

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
        return render(request, 'html/index.html')

    def post(self, request):

        pass


class DashboardView(APIView):

    def get(self, request):

        pass

    def post(self, request):

        pass


#below is code for many APIs.