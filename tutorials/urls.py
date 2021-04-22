from django.conf.urls import url 
from tutorials import views 
 
urlpatterns = [ 
    url('advisor', views.tutorial_list),
    url('user/(?P<pk>[0-9]+)$', views.tutorial_detail),
    url('user/advisor/(?P<pk>[0-9]+)$', views.booking_list),
    url('user/(?P<pk>[0-9]+)$advisor/bookings', views.booking_list),
]