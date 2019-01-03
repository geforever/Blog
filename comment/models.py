from django.db import models
from django.utils import timezone
from login.models import User
from personal_blog.models import Blog
# Create your models here.


class Comment(models.Model):
    comment_user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_content = models.CharField(max_length=256, null=False)
    comment_time = models.DateTimeField(auto_now_add=True)
    comment_blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment_content[:20]
    class Meta:
        ordering = ('comment_time',)