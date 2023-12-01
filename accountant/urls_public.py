from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = 'ACCOUNTS MONITOR'
admin.site.site_title = 'ACCOUNTS MONITOR'
admin.site.index_title = 'SITE ADMNISTRATION'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('homepage.urls')),
    path('blog/', include('blog.urls')),
    path('users/', include('users.urls')),
    path('register/', include('clients.urls')),
    path('sale_rep/', include('refferals.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)