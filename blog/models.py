from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #auth라는 앱의 User 모델과 FK를 맺겠다!
    #author = models.ForeignKey(settings.AUTH_USER_MODEL) #위와 동일한 내용임. 위는 이해를 위해 풀어씀.

    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
