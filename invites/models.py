from django.db import models


class Invite(models.Model):
    class Meta:
        ordering = ["id"]

    is_accept = models.BooleanField(default=False)

    is_admin = models.BooleanField(default=False)

    contact = models.ForeignKey(
        "contacts.Contact",
        on_delete=models.CASCADE,
        related_name="invites",
    )

    task = models.ForeignKey(
        "tasks.Task",
        on_delete=models.CASCADE,
        related_name="invites",
    )
