from django.conf.urls import url

from one import views

urlpatterns=[
    url(r'^home/',views.home,name='home'),
    url(r'^homelogin/',views.home_logined,name='homelogin'),
    url(r'^wodesc/',views.wodesc,name='wodesc'),
    url(r'^homelogincollect/',views.home_logined_collected,name='homelogincollect'),
    url(r'^delwodesc/',views.delwodesc,name='delwodesc'),

    url(r'^login/',views.login,name='login'),
    url(r'^dologin/',views.dologin,name='dologin'),

    url(r'^register/',views.register,name='register'),
    url(r'^doregister/',views.doregister,name='doregister'),
    url(r'^jianceuser/',views.jianceuser,name='jianceuser'),

    url(r'^userinfo/',views.userinfo_mod,name='userinfo'),
    url(r'^douserinfo/',views.douserinfo_mod,name='douserinfo'),
]