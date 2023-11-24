from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from hex.views import PeopleViewSet, AvaliadorViewSet, EquipeViewSet, EmpresaViewSet

router = DefaultRouter()
router.register(r"avaliador", AvaliadorViewSet)
router.register(r"empresa", EmpresaViewSet)
router.register(r"equipe", EquipeViewSet)
router.register(r"peoples", PeopleViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
    path("api/", include(router.urls)),
]

