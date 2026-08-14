from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ("STUDENT", "Student"),
        ("TEACHER", "Teacher"),
        ("ADMIN", "Admin"),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="STUDENT",
    )

    avatar = models.URLField(
        blank=True,
        null=True,
    )