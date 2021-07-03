from rest_framework import serializers
from tasker_business.models import (
    TaskerSkill,
    BusinessPhoto,
    Timeslot,
    TaskerAvailability,
)


class BusinessPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessPhoto
        fields = "__all__"


class TaskerSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskerSkill
        fields = "__all__"


class TimeslotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeslot
        fields = "__all__"


class TaskerAvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskerAvailability
        fields = "__all__"
