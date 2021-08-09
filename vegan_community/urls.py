from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('detail/', include("detail.urls")),
    path('blog/', include('blog.urls')),
    path('signup/', include('signup.urls')),
    path('vegan_admin/', include('vegan_admin.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('market/', include('market.urls')),
    path('', include('main.urls')),
]
