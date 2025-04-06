from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        related_name='followers',
        blank=True
    )

    def __str__(self):
        return self.username

    def follow(self, user):
        """Utility method to follow another user."""
        if user != self:
            self.following.add(user)

    def unfollow(self, user):
        """Utility method to unfollow another user."""
        if user != self:
            self.following.remove(user)

