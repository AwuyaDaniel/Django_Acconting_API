from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('chartofaccount', views.ChartOfAccountView)
router.register('groupchartofaccount', views.GroupOfChartOfAccountView)
router.register('chartofaccounttype', views.ChartOfAccountTypeView)

# App_name = 'Accounting'

urlpatterns = [
    path('', include(router.urls))
]
