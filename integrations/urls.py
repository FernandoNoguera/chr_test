from integrations.views import index,soup
from django.urls import path

urlpatterns = [
    path('', index),
    path('scraping/', soup),
]