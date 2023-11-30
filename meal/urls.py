from django.urls import path
from .views import show_items
urlpatterns = [
    path('show-item/', show_items, name='show-item'),
]
