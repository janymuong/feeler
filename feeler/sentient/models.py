# moodlens/sentient/models.py

from django.db import models
from django.contrib.auth.models import User

class SentimentHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sentiments')
    text = models.TextField()
    sentiment = models.CharField(max_length=20)  # e.g., "positive" or "negative"
    confidence = models.FloatField()  # Confidence score
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.sentiment} ({self.created_at})"
