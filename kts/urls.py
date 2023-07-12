from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from rest_framework.documentation import include_docs_urls
from main.views import CustomTokenObtainPairView


urlpatterns = [
    path("kts/", include("main.urls")),
    path("admin/", admin.site.urls),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('user-auth/', include('rest_framework.urls')),
    path('docs/', include_docs_urls(title='API Documentation')),
]
