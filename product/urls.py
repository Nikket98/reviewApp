from django.urls import path, re_path, include
from . import views
from django.contrib import admin
from .views import (
 
    ReviewUpdateView,
    ReviewDeleteView,
)

app_name = 'product'

urlpatterns = [
    
    path('<int:pk>/', views.product_detail, name='product-detail'),
    path('review/<int:pk>/', views.review_detail, name='review-detail'),
    path('list/', views.product_list, name='product-list'),
    path('review/<int:pk>/update/', ReviewUpdateView.as_view(), name='update-review'),
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='delete-review'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
]
