from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('addresses', views.AddressViewSet)

app_name = 'cab'

urlpatterns = [
    path('', include(router.urls))
]
