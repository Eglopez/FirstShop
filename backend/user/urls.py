from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'^users', views.UserView)

url_patterns = [
    path('', include(router.urls)),
]