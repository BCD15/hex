from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from hex.views import PeopleViewSet

router = DefaultRouter()
router.register(r"peoples", PeopleViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]