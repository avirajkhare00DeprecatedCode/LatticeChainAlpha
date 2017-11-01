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
from service1.views import SignupView, GetTickerView, CreateFakeTxn
from front_end.views import IndexView, LoginView, LogoutView, DashboardView, FetchPreBasketsView, FetchSubmitBasket, UserProfileView, MarketPlaceView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', SignupView.as_view(), name='signup_view'),
    url(r'^get_ticker/$', GetTickerView.as_view(), name='get_ticker_view'),
    url(r'^create_fake_txn/$', CreateFakeTxn.as_view(), name='create_fake_txn'),
    url(r'^$', IndexView.as_view(), name='index_page'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^dashboard/', DashboardView.as_view(), name='dashboard'),
    url(r'^profile/$', UserProfileView.as_view(), name='user_profile'),
    url(r'^marketplace/$', MarketPlaceView.as_view(), name='marketplace_view'),
    #below are api urls
    url(r'^api/v1/fetch_pre_baskets/$', FetchPreBasketsView.as_view(), name='fetch_pre_baskets'),
    url(r'^api/v1/fetch_submit_baskets/$', FetchSubmitBasket.as_view(), name='fetch_submit_basket')
]
