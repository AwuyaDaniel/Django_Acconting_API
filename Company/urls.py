from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('company', views.CompanyView)

# App_name = 'Accounting'

urlpatterns = [
    path('company', include(router.urls))
]
