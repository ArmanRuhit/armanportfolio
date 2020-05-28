from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("projects.urls")),
    path("blog/", include("blog.urls")),
    path('about/', include('about_me.urls'))
]