from django.contrib import admin
from django.urls import path, include
from main import views  # Assuming the views are in your 'main' app
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Allauth URLs for login
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('login/', auth_views.LoginView.as_view(template_name='jobllm/templates/account/login.html'), name='login'),

]
