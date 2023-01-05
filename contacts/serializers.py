from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["id", "name", "email", "phone_number"]

    def create(self, validated_data: dict) -> Contact:
        return Contact.objects.create(**validated_data)

    def update(self, instance: Contact, validated_data: dict) -> Contact:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
