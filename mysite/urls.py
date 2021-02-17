from django.urls import path
from django.contrib.auth.views import LogoutView
from mysite import views
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('', views.index),
    path('login/', views.Login.as_view()),
    path('logout/', LogoutView.as_view()),
    path('signup/', views.signup),
    path('mypage/', views.MypageView.as_view()),
    path('contact/', views.ContactView.as_view()),
    path('pay/', views.PayView.as_view()),
    path('article/', cache_page(30)(views.article)),
]
