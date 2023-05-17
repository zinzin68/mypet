from django.contrib import admin

from .models import Post

# Register your models here.
#관리자가 post에 접근할 수 있음
admin.site.register(Post)