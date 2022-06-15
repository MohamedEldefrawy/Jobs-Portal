from rest_framework import serializers
from job.models import Job
 
class JobSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Job
        depth = 1


class JobCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Job
