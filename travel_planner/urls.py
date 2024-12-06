# travel_planner/urls.py
from django.contrib import admin
from django.urls import path, include
from trips import views  # Import views from the trips app

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin interface
    path('trips/', include('trips.urls')),  # Include the URLs defined in the trips app
    path('', views.home, name='home'),  # Link the root URL to the home view
]
