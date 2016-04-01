from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):
    user = models.ForeignKey(User, related_name='data')
    votes = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'user_data'
        verbose_name = 'user data'
        verbose_name_plural = 'users data'

    def __str__(self):
        return self.user


class Restaurant(models.Model):
    res_id = models.IntegerField()
    name = models.CharField(max_length=191, blank=False, null=True)
    url = models.URLField()
    address = models.CharField(max_length=191, blank=False, null=True)
    locality = models.CharField(max_length=191, blank=True, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    cuisine = models.CharField(max_length=255, blank=True, null=True)
    avg_cost = models.IntegerField()
    rating = models.DecimalField()
    rating_text = models.CharField(max_length=191, blank=False, null=True)
    pic_url = models.URLField()
    menu_url = models.URLField()
    image_url = models.URLField()

    class Meta:
        db_table = 'restaurant_data'
        verbose_name = 'restaurant'
        verbose_name_plural = 'restaurants'

    def __str__(self):
        return self.name
