from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.contrib import admin
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landing.urls')),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug>/', views.blog_details, name='blog_details'),
    path('product/', include('product.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)