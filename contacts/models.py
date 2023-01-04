from django.db import models


class Contact(models.Model):

    class Meta:
        ordering = ["id"]

    name = models.CharField(max_length=127)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=20)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="contacts",)
