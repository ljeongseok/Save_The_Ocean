from django.contrib import admin
from board.models import *

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'title', 'modify_dt')


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ('comment_contents','post')