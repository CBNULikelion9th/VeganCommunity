from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('detail/', include("detail.urls")),
    path('blog/', include('blog.urls')),
    path('vegan_admin/', include('vegan_admin.urls')),
]
