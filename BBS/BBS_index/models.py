from django.db import models
from login.models import User
# Create your models here.


class Module(models.Model):#主题讨论
    module_name = models.CharField(max_length=32, unique=True)
    module_create_time = models.DateTimeField(auto_now_add=True)
    statement = models.TextField()#备注字段

    def __str__(self):
        return self.module_name

    class Meta:
        verbose_name = "主题"
        verbose_name_plural = "主题"


class Topic(models.Model):#帖子
    tID = models.ForeignKey(Module, on_delete=models.CASCADE)#Module的主键
    tUser = models.ForeignKey(User, on_delete=models.CASCADE)
    tTitle = models.CharField(max_length=32, null=False)
    tBody = models.TextField(null=False)
    tCreate_time = models.DateTimeField(auto_now_add=True)
    tViews = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.tTitle

    class Meta:
        ordering = ('-tCreate_time',)
        verbose_name = "帖子"
        verbose_name_plural = "帖子"

    def increate_tViews(self):
        self.tViews += 1
        self.save(update_fields=['tViews'])
