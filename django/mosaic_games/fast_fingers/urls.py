from django.urls import path

from . import views

urlpatterns = [
    path('', views.type, name='type'),
    path('login/', views.login_page, name='login'),
    path('auth/', views.login_user, name='authorize'),
    path('logout/', views.logout_user, name='logout'),
    path('get_page/', views.get_user_input, name='get_user_input'),
    path('calculate_all_scores/', views.calculate_all_scores, name='calculate_all_scores'),
    path('display_score/', views.display_score, name='display_score'),
]
