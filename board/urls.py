#from django.urls import path
from django.conf.urls import url
from .views import DashHome
urlpatterns = [
    url('dash/',DashHome),
]
