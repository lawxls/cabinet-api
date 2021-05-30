from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

app_name = 'user'
urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.ObtainTokenView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/blacklist/', views.LogoutAndBlacklistRefreshTokenForUserView.as_view(), name='token_blacklist'),
    path('me/', views.ManageUserView.as_view(), name='me')
]
