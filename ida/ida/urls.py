from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .settings import MEDIA_URL, MEDIA_ROOT, STATIC_ROOT, STATIC_URL


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("app.urls"))

]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
