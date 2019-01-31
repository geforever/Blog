from django.db import models
from django.utils import timezone
from login.models import User
from personal_blog.models import Blog
from BBS.BBS_index.models import Topic
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
        verbose_name = "博客评论"
        verbose_name_plural = "博客评论"


class BBS_Comment(models.Model):
    BBScomment_user_id = models.ForeignKey(User, on_delete=models.CASCADE)#对应用户信息ID
    BBScomment_content = models.TextField(null=False)
    BBScomment_time = models.DateTimeField(auto_now_add=True)
    BBScomment_ID = models.ForeignKey(Topic, on_delete=models.CASCADE)#对应帖子ID
    def __str__(self):
        return self.BBScomment_content
    class Meta:
        ordering = ('BBScomment_time',)
        verbose_name = "帖子评论"
        verbose_name_plural = "帖子评论"