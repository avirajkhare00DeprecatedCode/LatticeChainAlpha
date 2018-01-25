"""projectx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from front_end.views import IndexView, LoginView, LogoutView, DashboardView, MarketPlaceView, MarketPlaceSellBasketView
from front_end.views import TokenizeAssetsView
from front_end.api_calls import AddUserToken, GetUserTokens, TokenBasketOrderAPI

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^signup/$', SignupView.as_view(), name='signup_view'),
    url(r'^$', IndexView.as_view(), name='index_page'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^dashboard/', DashboardView.as_view(), name='dashboard'),
    url(r'^marketplace/$', MarketPlaceView.as_view(), name='marketplace_view'),
    url(r'^marketplace/sell_token_basket/$', MarketPlaceSellBasketView.as_view(), name='sell_token_basket'),
    url(r'^marketplace/tokenize_assets/$', TokenizeAssetsView.as_view(), name='tokenize_assets'),
    #url(r'^profile/$', UserProfileView.as_view(), name='user_profile'),
    #url(r'^marketplace/sell/$', MarketPlaceSellView.as_view(), name='marketplace_sell_view'),
    #url(r'^marketplace/buy/$', MarketPlaceBuyView.as_view(), name='marketplace_sell_view'),
    #below are api urls
    url(r'^api/v1/add_user_token/$', AddUserToken.as_view(), name='add_user_token'),
    url(r'^api/v1/get_user_tokens/$', GetUserTokens.as_view(), name='get_user_tokens'),
    url(r'^api/v1/token_basket_order/$', TokenBasketOrderAPI.as_view(), name='token_basket_order'),
    #url(r'^api/v1/fetch_pre_baskets/$', FetchPreBasketsView.as_view(), name='fetch_pre_baskets'),
    #url(r'^api/v1/fetch_submit_baskets/$', FetchSubmitBasket.as_view(), name='fetch_submit_basket'),
    #url(r'^api/v1/submit_basket_marketplace/$', MarketPlaceApi.as_view(), name='buy_sell_send'),
    #url(r'^api/v1/fetch_buy_basket_marketplace/$', MarketPlaceApi.as_view(), name='buy_baskets_marketplace')
]
