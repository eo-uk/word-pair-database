from enum import auto
from django.db import models

# Create your models here.
class WordPair(models.Model):
    sourceLang = models.CharField(max_length=32)
    sourceWord = models.CharField(max_length=64)
    targetLang = models.CharField(max_length=32)
    targetWord = models.CharField(max_length=64)
    field = models.CharField(max_length=64, default="general")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    isBeingEdited = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.sourceWord} ({self.sourceLang}) - {self.targetWord} ({self.targetLang}) - {self.field}"

    class Meta:
        ordering = ('pk',)
