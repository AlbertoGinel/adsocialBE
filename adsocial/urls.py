from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Default admin route
    path('api/', include('influencers.urls')),  # Include the influencers app URLs
]