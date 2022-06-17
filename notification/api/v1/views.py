from notification.models import Notification
from rest_framework import status, decorators
from rest_framework.response import Response

from .serializers import NotificationSerialize


@decorators.api_view(["GET"])
def get(request, user_id):
    notifications = Notification.objects.filter(users_id=user_id).all()
    serialize = NotificationSerialize(notifications, many=True)
    return Response({'success': True, 'notifications': serialize.data}, status=status.HTTP_200_OK)
