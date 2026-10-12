from django.contrib import admin
from django.urls import include, path
from django.shortcuts import render
from tasks.views import health_check

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("tasks.urls")),
    path("api/health/", health_check, name="health-check"),
    path("", lambda request: render(request, "index.html"), name="ui"),
]
