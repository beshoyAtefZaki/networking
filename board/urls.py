from django.urls import path
from .views import DashHome
urlpatterns = [
    path('dash/',DashHome),
]
