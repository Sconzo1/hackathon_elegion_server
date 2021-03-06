from django.contrib import admin
from django.urls import path, include


admin.site.site_header = "Панель управление e-Legion"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('auth/', include('authentication.urls')),
    path('chats/', include('chats.urls')),
    path('redmine/', include('redmine.urls')),
    path('', include('spectacular.urls')),
    # path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
