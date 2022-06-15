from rest_framework import serializers
from job.models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['creator', 'name', 'description', 'tags', 'banner_img',
                  'status', 'accepted_dev', 'user_marked_done', 'creator_marked_done']
        model = Job
        depth = 1


class JobCreateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Job
