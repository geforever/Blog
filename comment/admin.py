from django.contrib import admin
from .models import Comment, BBS_Comment

# Register your models here.
admin.site.register(Comment)
admin.site.register(BBS_Comment)
