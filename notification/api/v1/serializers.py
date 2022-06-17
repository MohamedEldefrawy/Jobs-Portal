from notification.models import Notification
from rest_framework import serializers


class NotificationSerialize(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ["message", "creation_time", "status"]
        depth = 1
