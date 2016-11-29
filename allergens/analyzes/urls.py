from django.conf.urls import url, include
from analyzes.views import *

urlpatterns = [
    url(r'^$', analyzes, name = 'analyzes'),
]