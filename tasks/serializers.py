from rest_framework import serializers
from contacts.models import Contact
from invites.models import Invite
from users.models import User
from utils.send_invite import check_email, send_invite_from_list
from .models import Task


class GuestSerializer(serializers.Serializer):
    email = serializers.EmailField()
    is_admin = serializers.BooleanField()


class TaskSerializer(serializers.ModelSerializer):
    guests = GuestSerializer(
        many=True,
        write_only=True,
    )
    guests_list = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            "id",
            "name",
            "description",
            "time_course",
            "schedule_time",
            "schedule_date",
            "status",
            "created_at",
            "updated_at",
            "priority",
            "category",
            "guests",
            "guests_list",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]

    def get_guests_list(self, obj):
        invites = list(Invite.objects.filter(task_id=obj.id))
        data = []
        for invite in invites:
            contact = Contact.objects.get(pk=invite.contact_id)
            data.append(contact.email)
        return data

    def create(self, validated_data: dict) -> Task:
        user_obj = validated_data.pop("owner")
        guest_list = validated_data["guests"]

        check_email(guest_list, user_obj.id)

        task_obj = Task.objects.create(**validated_data, user=user_obj)
        send_invite_from_list(guest_list, task_obj, user_obj)

        return task_obj

    def update(self, instance: Task, validated_data: dict) -> Task:

        for key, value in validated_data.items():
            setattr(instance, key, value)
        try:
            email_list = validated_data["guests"]
        except KeyError:
            raise serializers.ValidationError({"detail": f"guests field is required"})

        check_email(email_list, instance.user_id)

        Invite.objects.filter(task_id=instance.id).delete()

        user_obj = User.objects.get(id=instance.user_id)
        send_invite_from_list(email_list, instance, user_obj)

        instance.save()
        return instance
