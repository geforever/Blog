from django.db import models
from login.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=128, blank=True)#昵称
    bio = models.TextField(max_length=500, blank=True)#个性签名
    birthday = models.CharField(max_length=20, default='1980-01-01')#出生日期
    avatar = models.ImageField(upload_to='avatar/%Y%m%d', blank=True, default='avatar/default.jpg')

    class Meta:
        verbose_name = "个人信息"
        verbose_name_plural = "个人信息"

    def __str__(self):
        return 'user {}'.format(self.user.user_name)
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

