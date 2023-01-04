from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = ["id", "name", "description", "time_course", "schedule_time", "schedule_date","status","created_at","updated_at","priority","user_id", "categories_id"]
    read_only_fields = ["id", "created_at", "updated_at"]