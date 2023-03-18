from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('journal_entry', views.JournalEntryView)
router.register('account_entries', views.AccountEntriesView)

# App_name = 'Accounting'

urlpatterns = [
    path('journal_entry', include(router.urls))
]
