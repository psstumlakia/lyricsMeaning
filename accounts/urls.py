from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import register, view_profile, edit_profile, change_password
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetView, PasswordResetCompleteView,
                                       PasswordResetDoneView, PasswordResetConfirmView,)


urlpatterns = [
    #path('', home, name='index'),
    #path('index/', home, name=''),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', view_profile, name='profile'),
    url(r'^profile/(?P<pk>\d+)/$', view_profile, name='profile_with_pk'),
    path('profile/edit', edit_profile, name='profileEdit'),
    path('change_password/', change_password, name='change_password'),
    #   password Resetting Section
    path('password_reset/', PasswordResetView.as_view(template_name='accounts/reset_password.html'),
         name='reset_password'),
    path('password_reset/done/',
         PasswordResetDoneView.as_view(template_name='accounts/reset_password_done.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='accounts/reset_password_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset/complete/',
         PasswordResetCompleteView.as_view(template_name='accounts/reset_password_complete.html'),
         name='password_reset_complete'),
]
