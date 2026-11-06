
import uuid
from django.db import models


class BirthdayWish(models.Model):

    THEME_CHOICES = [
        ('classic', 'Classic Birthday'),
        ('romantic', 'Romantic Wish'),
        ('photo_gallery', 'Photo Gallery'),
        ('surprise', 'Surprise Box'),
        ('cake_theme', 'Cake Celebration'),
        ('cinematic', 'Cinematic'),
        ('minimal', 'Minimal'),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    card_title = models.CharField(max_length=150)

    sender_name = models.CharField(max_length=100)

    birthday_person = models.CharField(max_length=100)

    age = models.PositiveSmallIntegerField()

    message = models.TextField(max_length=2000)

    image = models.ImageField(
        upload_to="birthday_photos/",
        null=True,
        blank=True
    )

    # Selected birthday layout
    theme = models.CharField(
        max_length=30,
        choices=THEME_CHOICES,
        default='classic'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.card_title} - {self.birthday_person}"

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Birthday Wish"
        verbose_name_plural = "Birthday Wishes"


# Additional Birthday Photos
class BirthdayImage(models.Model):

    birthday = models.ForeignKey(
        BirthdayWish,
        on_delete=models.CASCADE,
        related_name='photos'
    )

    image = models.ImageField(
        upload_to="birthday_memories/"
    )

    message = models.CharField(
        max_length=255,
        blank=True
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["uploaded_at"]

    def __str__(self):
        return f"Photo for {self.birthday.birthday_person}"
