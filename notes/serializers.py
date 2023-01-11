from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "description", "created_at", "updated_at", "user_id"]
        read_only_fields = ["id", "created_at", "updated_at", "user_id"]

        def create(self, validated_data):
            return Note.objects.create(**validated_data)

        def update(self, instance, validated_data):
            for key, value in validated_data.items():
                setattr(instance, key, value)

            instance.save()
            return instance
