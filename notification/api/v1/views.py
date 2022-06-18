from notification.models import Notification
from rest_framework import status, decorators
from rest_framework.response import Response

from .serializers import NotificationSerialize


@decorators.api_view(["GET"])
def get(request, user_id):
    notifications = Notification.objects.filter(users_id=user_id).all()
    serialize = NotificationSerialize(notifications, many=True)
    return Response({'success': True, 'notifications': serialize.data}, status=status.HTTP_200_OK)


@decorators.api_view(["PUT"])
def update(request, notification_id):
    selected_notification = Notification.objects.filter(id=notification_id).first()
    if selected_notification.status == "true":
        selected_notification.status = "false"
    else:
        selected_notification.status = "true"
    selected_notification.save()
    return Response({'success': True, 'message': "Status has been update successfully"})
