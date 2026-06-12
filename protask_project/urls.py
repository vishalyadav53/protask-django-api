from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# 1. Normal tarike se schema view banayein
schema_view = get_schema_view(
   openapi.Info(
      title="ProTask API",
      default_version='v1',
      description="Management and Collaboration API Documentation",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# 2. Swagger ko batayein ki humein sirf Bearer Token (Taala) chahiye
schema_view.security_definitions = {
    'Bearer': {
        'type': 'apiKey',
        'name': 'Authorization',
        'in': 'header',
        'description': "Format: Bearer <your_jwt_token>"
    }
}

# 3. Clean aur simple URL patterns
urlpatterns = [
    # Homepage kholte hi Swagger par bhejo
    path('', RedirectView.as_view(url='swagger/', permanent=False)),

    # Admin Panel
    path('admin/', admin.site.urls),
    
    # Core App (Tasks) URLs 
    path('api/', include('core.urls')),

    # JWT Authentication Endpoints (Login aur Refresh)
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Swagger Documentation Links
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]