from django.db import models


class Response(models.Model):
    phrase = models.CharField(max_length=255)
    response = models.TextField()

    def __str__(self):
        return self.phrase
