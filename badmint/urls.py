from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework import routers

from api.views import SwaggerSchemaView, ViewCategory, ViewRanking, FileViewSet, RankingClassificationViewset

router = routers.DefaultRouter()
router.register(r'category', ViewCategory)
#router.register(r'file', FileViewSet)
router.register(r'ranking', ViewRanking)
router.register(r'ranking-query', RankingClassificationViewset)

urlpatterns = [
                  path('', lambda req: redirect('/admin/')),
                  path('admin/', admin.site.urls),
                  path('api/v1/', include(router.urls)),
                  path('api/v1/docs/', SwaggerSchemaView.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
