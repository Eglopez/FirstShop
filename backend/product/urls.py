from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'^products', views.ProductView)

url_patterns = [
    path('', include(router.urls)),
]