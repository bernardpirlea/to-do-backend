from django.db import models

# Create your models here.


class ToDo(models.Model):
    text = models.CharField(max_length=150)
    done = models.BooleanField(default=False)
    last_modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.text
