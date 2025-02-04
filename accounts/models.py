from django.db import models
from django.conf import settings


class Country(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=5)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'countries'
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.BigIntegerField(unique=True, null=True, blank=True)
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, upload_to='profile_avatars/')


class Device(models.Model):
    DEVICE_WEB = 1
    DEVICE_IOS = 2
    DEVICE_ANDROID = 3
    DEVICE_PC = 4
    DEVICE_TYPE_CHOICES = (
        (DEVICE_WEB, 'Web'),
        (DEVICE_IOS, 'IOS'),
        (DEVICE_ANDROID, 'Android'),
        (DEVICE_PC, 'PC'),
    )

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='devices', on_delete=models.CASCADE)
    device_uuid =models.UUIDField('device UUID', null=True)
    last_login = models.DateTimeField('last login date', null=True)
    device_type = models.PositiveSmallIntegerField(choices=DEVICE_TYPE_CHOICES, default=DEVICE_WEB)
    device_os = models.CharField('device os', max_length=20, blank=True)
    device_model = models.CharField('device model', max_length=50, blank=True)
    app_version = models.CharField('app version', max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)