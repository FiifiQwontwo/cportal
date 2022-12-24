from django.urls import path
from .views import register, login, logout, activate

app_name = 'accounts'

urlpatterns = [
    path('signup/', register, name='signup_url'),
    path('login/', login, name='login_url'),
    path('logout/', logout, name='sign_out_url'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    # path('forgot/', forgotpassword, name='password_reset_url'),
    # path('reset/<uidb64>/<token>/', reset_password_validate, name='validate_password_url'),
]
