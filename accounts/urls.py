from django.urls import path
from .views import register, login, logout, activate

app_name = 'accounts'

urlpatterns = [
    path('signup/', register, name='signup_url'),
    path('login/', login, name='login_url'),
    path('logout/', logout, name='sign_out_url'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
   
]
