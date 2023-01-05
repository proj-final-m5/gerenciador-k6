from rest_framework import serializers
from invites.serializers import InviteSerializer
from .models import Task
from contacts.models import Contact
from django.shortcuts import get_object_or_404
from invites.views import invite
import ipdb


class TaskSerializer(serializers.ModelSerializer):
    # guests = InviteSerializer(many=True)

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
            "user_id",
            "category",
            # "guests",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
        # extra_kwargs = {"guests": {"write_only": True}}

        def create(self, validated_data: dict):
            ipdb.set_trace()
            print()
            email_list = validated_data.pop("guests")
            print(email_list)

            task_obj = Task.objects.create(**validated_data)

            for email in email_list:
                contacts = Contact.objects.get(email=email)
                contact_exists = get_object_or_404(contacts, email=email)
                invite(
                    assunto=task_obj.category,
                    link="http://127.0.0.1:8000/email/",
                    email=email,
                )

            return task_obj

        def update(self, instance, validated_data):
            for key, value in validated_data.items():
                setattr(instance, key, value)

                instance.save()
                return instance
