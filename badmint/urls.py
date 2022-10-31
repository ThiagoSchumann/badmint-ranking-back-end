from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from rest_framework import routers

from api.views import SwaggerSchemaView

router = routers.DefaultRouter()


urlpatterns = [
    path('', lambda req: redirect('/api/v1/')),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/docs/', SwaggerSchemaView.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
