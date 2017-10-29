from django.shortcuts import render, HttpResponse
# Create your views here.
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#from service1.core.get_wallet_ids import generate_keys
from service1.core.parse_ticker import get_current_price

from service1.models import User
from service1.models import UserDetails, CryptoCoins, ERC20Tokens, TransactionData

class GetTickerView(APIView):

    def get(self, request):

        if CryptoCoins.objects.filter(coin_id=request.GET['coin_id']).exists():

            return HttpResponse(get_current_price(CryptoCoins.objects.get(coin_id=request.GET['coin_id']).ticker_api, 'coin', request.GET['coin_id']))

        if ERC20Tokens.objects.filter(token_id=request.GET['coin_id']).exists():

            return HttpResponse(ERC20Tokens.objects.get(token_id=request.GET['coin_id']).ticker_api, 'erc20', request.GET['coin_id'])


class CreateFakeTxn(APIView):

    def get(self, request):

        return HttpResponse('only post shit!')

    def post(self, request):

        #will add backend validation and logic later

        new_transaction = TransactionData()
        new_transaction.json_data_current = request.POST['txn_data']
        new_transaction.save()

        return HttpResponse(200)


class SignupView(APIView):

    def get(self, request):

        return render(request, 'signup.html')

    def post(self, request):

    """

        new_user = User()

        new_user.username = request.POST['username']
        new_user.email = request.POST['email']
        new_user.check_password(request.POST['password'])

        new_user.save()

        new_keys = generate_keys()

        print new_keys

        new_user = UserDetails()

        new_user.userid = User.objects.get(username=request.POST['username'])

        new_user.full_name = request.POST['full_name']
        new_user.contact_number = request.POST['contact_number']

        new_user.neo_public_key = new_keys[0]['neo_public_key']
        new_user.neo_private_key = new_keys[0]['neo_private_key']

        new_user.bitcoin_public_key = new_keys[1]['bitcoin_public_key']
        new_user.bitcoin_private_key = new_keys[1]['bitcoin_private_key']

        new_user.save()

    """

        return HttpResponse("check database now")

