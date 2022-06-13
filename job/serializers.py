from rest_framework import serializers

from .models import Job


class JobSerializer(serializers.ModelSerializer):
    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = Job
        fields = ['id', 'name', 'description', 'banner', 'tags']
        depth = 1
