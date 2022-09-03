from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from api.sorts import views as sort_views
from api.searchings import views as searching_views

schema_view = get_schema_view(
    openapi.Info(
        title="알고리즘 시각화 API",
        default_version='프로젝트 버전 ( 1.0 )',
        description="API 명세서",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

routers = DefaultRouter()

routers.register("sorts", sort_views.SortViewSet, basename="sorts")
routers.register("searchings", searching_views.SearchViewSet, basename="searchings")

urlpatterns = [
    #path('admin/', admin.site.urls),
    path(r"api-v1/", include(routers.urls)),
    path('__debug__/', include('debug_toolbar.urls')),

    path(r'api-v1/algo_visualizer/swagger(?P<format>\.json|\.yaml)',
         schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'api-v1/algo_visualizer/swagger', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path(r'api-v1/algo_visualizer/redoc', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc-v1'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
