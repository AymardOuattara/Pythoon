from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from caisse.views import Paniers,PanierDetail,Vente

schema_view = get_schema_view(
    openapi.Info(
        title="Notes API POUR IGESCOM REFONTE",
        default_version='v1',
        description="Notes API POUR IGESCOM REFONTE",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@ldfgroupe.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/articles/', include('caisse.urls')),
    path('api/panier/', Paniers.as_view()),
    path('api/paniers/<str:pk>', PanierDetail.as_view()),
    path('api/vente/', Vente.as_view()),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
            cache_timeout=0), name='schema-redoc'),
]

