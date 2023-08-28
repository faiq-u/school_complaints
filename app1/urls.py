from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('add_comp/',views.add_comp,name='add_comp'),
    path('auth1/',views.auth1,name='auth1'),
    path('auth2/',views.auth2,name='auth2'),
    path('sd/',views.sd,name='sd'),
    path('pc/',views.pc,name='pc'),
    path('register/',views.register_user,name='register'),
    path('login/',views.login,name='login'),
    path('add_comp/register/',views.fix2,name='fix2'),
    path('add_comp/login/',views.fix,name='fix')
]

