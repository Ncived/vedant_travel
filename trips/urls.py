from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from trips import views
from django.contrib import admin

urlpatterns = [
    path('', views.destination_list, name='destination_list'),
    path('<int:pk>/', views.destination_detail, name='destination_detail'),
    path('<int:destination_pk>/book/', views.booking_create, name='booking_create'),
    path('', views.home, name='home'),
    path('new/', views.destination_create, name='destination_create'),  # Form to create new destination
    path('<int:pk>/edit/', views.destination_update, name='destination_update'),  # Edit existing destination
    path('<int:pk>/delete/', views.destination_delete, name='destination_delete'), 
    path('signup/', views.signup, name='signup'),  # Custom signup view
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Built-in login view
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Built-in logout view
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page
]


