from django.urls import path, include

urlpatterns = [
    path('api/', include('api.urls')),
    path('auth/', include('authentication.urls')),
    path('chats/', include('chats.urls')),
    path('', include('spectacular.urls')),
    # path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
