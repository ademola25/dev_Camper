from rest_framework import serializers
from .models import Courses


class CoursesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Courses
        fields = ['title', 'description','weeks','tuition', 'minimumSkill', 'scholarhipsAvailable', 
    'bootcamp']
