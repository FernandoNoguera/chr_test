from integrations.views import index,soup
from django.urls import path

urlpatterns = [
    path('', index, name='home'),
    path('scraping/', soup, name='scraping'),
]