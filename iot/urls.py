from django.urls import path, include
from rest_framework import routers
from .api import StateViewSet
from .views import home

router = routers.DefaultRouter()
router.register('state', StateViewSet)

urlpatterns = [
    path('api/', include(router.urls)),   # API endpoints
    path('', home, name='home'),          # homepage → http://127.0.0.1:8000/
    path('home/', home, name='home2'),    # optional → http://127.0.0.1:8000/home/
]
