from django.urls import path
from django.views.generic import TemplateView
from . import views
from accounts.views import profile,Login,Register

urlpatterns = [
    path('login/',Login.as_view() ,name='login'),
    path('',views.home,name='home'),
    path('signup/',Register.as_view(), name='signup'),
    path('profile/',profile.as_view(), name='profile'),
    path('logout/',views.logout_view,name='logout'),
]