from .views import (
    FirstAPI,
    HomePage,
)
from django.urls import path


urlpatterns = [
    path('first-api', FirstAPI.as_view(), name="first_api", ),
    path('', HomePage.as_view(), name="home", ),
]