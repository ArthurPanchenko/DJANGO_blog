from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Profile(models.Model):
    """Model for user's profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username}'s profile"


class Post(models.Model):
    """Model for post"""

    title = models.CharField('Title', max_length=255)
    content = models.TextField('Text')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_date = models.DateField(auto_now_add=True, editable=False)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return self.title
