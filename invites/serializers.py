from rest_framework import serializers
from .models import Invite


class InviteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invite
        fields = [
            "id",
            "contact_id",
            "task_id",
            "is_accept",
            "is_admin",
        ]

    def create(self, validated_data: dict) -> Invite:
        return Invite.objects.create(**validated_data)

    def update(self, instance: Invite, validated_data: dict) -> Invite:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
