"""Models object defined in our applicaiton."""
from django.db import models

# Create your models here.
from django.utils import timezone


class Post(models.Model):
    """Model for a Post object."""

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        """Method to publish the post."""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """Method to display the post in the command line."""
        return self.title
