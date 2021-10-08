from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model



class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    image = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", args=[self.id])
