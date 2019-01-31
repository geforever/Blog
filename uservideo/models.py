from django.db import models
from login.models import User
from django.utils import timezone

# Create your models here.
class Uservideo(models.Model):
    video_owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    video_name = models.CharField(max_length=128, null=False)
    video_create_time = models.DateTimeField(default=timezone.now())
    video_path = models.CharField(max_length=256, null=False)

    def __str__(self):
        return self.video_name

    class Meta:
        ordering = ('video_create_time',)
        verbose_name = "视频"
        verbose_name_plural = "视频"
