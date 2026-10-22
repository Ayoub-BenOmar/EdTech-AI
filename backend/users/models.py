from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ("STUDENT", "Student"),   # APPRENANT in the brief
        ("ADMIN", "Admin"),       # ADMINISTRATEUR in the brief
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="STUDENT")
    avatar = models.URLField(blank=True, null=True)

    # Quotas (editable by admins)
    max_documents = models.PositiveIntegerField(default=20)
    max_storage_bytes = models.BigIntegerField(default=500 * 1024 * 1024)  # 500 MB

    email = models.EmailField(unique=True)  # email is the login identity in the brief

    @property
    def is_admin_role(self):
        return self.role == "ADMIN"