from django.urls import path
from .views import *

app_name='stray'

urlpatterns = [
    path('', index),
    path('post_list', post_list),
]