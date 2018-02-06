from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.PROTECT) # ForeinKey definiert eine Verlinkung zu einem anderen Modell
    title = models.CharField(max_length=200) # CharField wird fuer limitierte, kurze Texte verwendet
    text = models.TextField()                 # TextField wird fuer lange Texte verwendet
    created_date = models.DateTimeField(    # DateTimeField ist ein Feld fuer Datum und Zeit
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
