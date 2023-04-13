from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    path('signup/',views.signup, name='signup'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('<int:account_pk>/detail/', views.detail, name='detail'),
    path('password/',views.password_change,name='password_change'),
    
]
