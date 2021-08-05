from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='register'),
    path('register/done', UserCreateDoneView.as_view(), name='register_done'),
]
