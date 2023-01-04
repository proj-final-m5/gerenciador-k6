from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = ["id", "name", "description", "time_course", "schedule_time", "schedule_date","status","created_at","updated_at","priority","user_id", "category"]
    read_only_fields = ["id", "created_at", "updated_at"]

    def create(self, validated_data):
        return Task.objects.get_or_create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance