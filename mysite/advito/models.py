from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
def user_avatar_path(instance, filename):
    return 'user_{0}/foto/{1}'.format(instance.user.id, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name='пользователь')
    about = models.TextField(max_length=500, verbose_name='о себе')
    avatar = models.ImageField(upload_to=user_avatar_path, verbose_name='фото пользователя')
    birth_date = models.DateField(null=True, blank=True, verbose_name='день рождения')
    created = models.DateTimeField(default=timezone.now)