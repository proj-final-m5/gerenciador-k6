from rest_framework import serializers

from contacts.models import Contact
from invites.models import Invite
from users.models import User
from utils.send_invite import send_invite

from .models import Task


class TaskSerializer(serializers.ModelSerializer):

    guests = serializers.ListSerializer(
        child=serializers.CharField(), write_only=True)
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
            "guests_list"
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

        email_list = validated_data["guests"]

        for email in email_list:
            contacts = list(Contact.objects.filter(
                user_id=user_obj.id, email=email))

            if not contacts:
                raise serializers.ValidationError(
                    {"detail": f"Email {email} not found in contacts"})

        task_obj = Task.objects.create(**validated_data, user=user_obj)

        for email in email_list:
            contacts = list(Contact.objects.filter(
                user_id=user_obj.id, email=email))

            invite_obj = Invite.objects.create(
                contact=contacts[0], task=task_obj)
            invite_obj.save()

            assunto = task_obj.category
            user = User.objects.get(pk=task_obj.user_id)
            schedule = f"Olá, o usuário {user.username}, agendou a {task_obj.name}, no dia {task_obj.schedule_date} às {task_obj.schedule_time}"
            link = f"http://127.0.0.1:8000/api/user/invite/{invite_obj.id}/"
            send_invite(assunto, schedule, link, email)

        return task_obj

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

            instance.save()
            return instance
