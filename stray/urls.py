from django.contrib import admin
from django.urls import path
#index 는 대문 post_list는 게시판
from stray.views import index, post_list, posting

app_name='stray'

urlpatterns = [
    path('admin/',admin.site.urls),
    path('', index,name='index'),
    path('post_list/', post_list, name='post_list'),
    path('post_list/<int:pk>/',posting, name='posting'),
]