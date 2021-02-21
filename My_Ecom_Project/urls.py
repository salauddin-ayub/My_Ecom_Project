from django.contrib import admin
from django.urls import path, include
from AppLogin import views


# To show media files
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppShop.urls')),
    path('account/', include('AppLogin.urls')),
    path('shop/', include('AppOrder.urls')),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)