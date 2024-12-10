from django.contrib import admin
from django.urls import path, include
from trips import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('trips/', include('trips.urls')),  # Include the URLs defined in the trips app
    path('', views.home, name='home'),  # Root URL linked to the home view
]
