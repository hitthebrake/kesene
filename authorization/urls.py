from django.urls import path

from . import views

app_name = 'authorization'
urlpatterns = [
    path('', views.login_view),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('add_organization/', views.add_organization, name='add_organization'),
    path('add_user/', views.add_user, name='add_user'),
    path('deleted_users/', views.deleted_users_view, name='deleted_users'),
    path('off_users/', views.off_users_view, name='off_users'),
    path('users/', views.users_view, name='users'),
]