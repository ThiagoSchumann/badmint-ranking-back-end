from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from rest_framework import routers, settings

from api.views import SwaggerSchemaView, ViewCategoryMock, ViewRankingMock, FileViewSet

router = routers.DefaultRouter()
#router.register(r'ranking-query', ViewRankingQueryMock)
router.register(r'file', FileViewSet)



urlpatterns = [
    path('', lambda req: redirect('/api/v1/')),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/docs/', SwaggerSchemaView.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/v1/category/', ViewCategoryMock.as_view()),
    path('api/v1/ranking/', ViewRankingMock.as_view()),
    #path('api/v1/ranking-query/', ViewRankingQueryMock.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
