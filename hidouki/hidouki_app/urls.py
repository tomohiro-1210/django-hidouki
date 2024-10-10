from django.urls import path
from .views import async_view, async_view2

urlpatterns = [
    path('async/', async_view, name="async"),
    path('async_view/', async_view2, name="async_view"),
]
