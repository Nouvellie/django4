from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("nouve-admin/", admin.site.urls),
]
