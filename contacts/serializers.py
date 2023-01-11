from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["id", "name", "email", "phone_number"]

    def create(self, validated_data: dict) -> Contact:
        contacts = Contact.objects.filter(
            user_id=validated_data["user_id"],
            email=validated_data["email"],
        )

        if contacts:
            email = validated_data["email"]
            raise serializers.ValidationError(
                {"detail": f"This contact {email} already exists."}
            )

        return Contact.objects.create(**validated_data)

    def update(self, instance: Contact, validated_data: dict) -> Contact:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
