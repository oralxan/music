from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/', include('apps.album.urls')),
    path('apis/', include('apps.music.urls')),
    path('apis/', include('apps.artist.urls')),
    path('apis/dj-rest-auth/', include('dj_rest_auth.urls'))
]
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)