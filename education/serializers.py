from rest_framework import serializers
from .models import Subject , Course


class SubjectSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):

    owner_name = serializers.SerializerMethodField()

    def get_owner_name(self , obj):
        return obj.owner.username
    class Meta:
        model = Course
        fields = '__all__'