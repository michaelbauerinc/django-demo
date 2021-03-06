from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    img = models.ImageField(
        default="./profile_pics/default.png", upload_to="profile_pics"
    )

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.img.path)
        width, height = img.size
        if width > 300 or height > 300:
            OUTPUT_SIZE = (300, 300)

            img.thumbnail(OUTPUT_SIZE)
            img.save(self.img.path)
