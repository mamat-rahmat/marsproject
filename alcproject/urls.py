from django.contrib import admin
from django.views.generic.base import RedirectView
from django.urls import path, include
from django.conf.urls.static import static
from alcproject import settings

admin.site.site_header = "MARS Competition"
admin.site.site_title = "MARS.COM Administration"
admin.site.index_title = "Administration | MARS Competition"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('', include('core.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
