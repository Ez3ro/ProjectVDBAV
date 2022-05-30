from django.contrib import admin
from .models import *
# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display = ('ParkerName', 'TimeIn')
admin.site.register(TimeIn_Out,CommentAdmin)
admin.site.register(Post)