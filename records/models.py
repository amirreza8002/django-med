from django.conf import settings
from django.db import models

from pictures.models import PictureField


class Image(models.Model):
    image = PictureField(upload_to="images/records")
    alt = models.CharField(max_length=255)

    def __str__(self):
        return f"image for {self.record.condition}"


class Medicine(models.Model):
    medicine = models.CharField(max_length=500)
    how_to_use = models.TextField()

    def __str__(self):
        return f"{self.medicine}"


class Record(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    condition = models.CharField(max_length=255)
    description = models.TextField()
    images = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="record")
    medicines = models.ManyToManyField(Medicine)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"condition: {self.condition} for {self.user}"

    def __repr__(self):
        return f"Record(user={self.user}, condition={self.condition})"
