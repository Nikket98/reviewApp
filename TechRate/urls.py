from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reviewApp.urls')),
    path('register/', user_views.register, name = 'register'),
    path('profile/', user_views.profile, name = 'profile'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name = 'logout'),
    path('users/', include('users.urls', namespace='users')),
    path('products/', include('product.urls', namespace='product')),
    path('api/', include('api.urls', namespace='api')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

