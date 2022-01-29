from rest_framework import serializers
from .models import Bootcamp


class BootcampSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bootcamp
        fields = ['name', 'slug','website','description','phone','email', 'address', 'careers', 
    'averageRating', 'averageCost','housing', 'jobAssitance',
    'jobGuarantee', 'acceptGi' ]