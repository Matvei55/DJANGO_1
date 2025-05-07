from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)  # unique=True обязательно!
    

    groups = models.ManyToManyField(
            Group,
            verbose_name='groups',
            blank=True,
            related_name="news_blog_user_set",
            related_query_name="news_blog_user",
        )
    user_permissions = models.ManyToManyField(
            Permission,
            verbose_name='user permissions',
            blank=True,
            related_name="news_blog_user_set",
            related_query_name="news_blog_user",
        )

    class Meta:
        db_table = 'users'