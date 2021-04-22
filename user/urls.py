
from django.conf.urls import url
from .views import CreateUserAPIView

urlpatterns = [
    url('register',CreateUserAPIView.as_view()),
]