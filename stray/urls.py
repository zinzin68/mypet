from django.contrib import admin
from django.urls import path
#index 는 대문 post_list는 게시판
from .views import index, new_post, post_list, posting, remove_post

from django.conf.urls.static import static
from django.conf import settings

app_name='stray'

urlpatterns = [
    path('admin/',admin.site.urls),

    path('', index,name='index'),

    path('post_list/', post_list, name='post_list'),

    path('post_list/<int:pk>/',posting, name='posting'),
    
    path ('post_list/new_post/',new_post, name='new_post'),
    
    path ('post_list/<int:pk>/remove/', remove_post, name='remove_post'),
]

#이미지 url 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)