from django.db import models

class Invite(models.Model):
    class Meta:
        ordering = ["id"]

    is_accept = models.BooleanField()

    contact_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="albums",
    )

    task_id = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="albums",
    )
