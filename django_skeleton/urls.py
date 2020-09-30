from django.conf.urls import url
from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt import views

schema_view = get_schema_view(
   openapi.Info(
      title="Project API",
      default_version='v1',
      description="Project description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="mail@domain.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
   # Swager URLs
   url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

   # Token URLs
   path('api/token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),

   # Apps URLs
   path('api/posts/', include('apps.posts.urls')),
   path('api/users/', include('apps.users.urls')),

   # Admin URL
   path('', lambda request: HttpResponse('<a href="/swagger">Swagger</a>, <a href="/redoc">Documentation</a>, <a href="/admin">Admin</a>')),
   path('admin/', admin.site.urls),
]
