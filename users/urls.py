from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    # Other URL patterns
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('check-security-answer/<int:user_id>/', views.check_security_answer, name='check_security_answer'),
    path('reset-password/<int:user_id>/', views.reset_password, name='reset_password'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html', success_url='/users/reset/done/'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]
