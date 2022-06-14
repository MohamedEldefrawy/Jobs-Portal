# Create your views here.
from rest_framework import permissions, decorators, response, status

from account.serializers import DeveloperCreateSerializer, CompanyCreateSerializer
from tag.models import Tag


@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def developer_registration(request):
    serializer = DeveloperCreateSerializer(data=request.data)
    if not serializer.is_valid(raise_exception=True):
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    user = serializer.save()
    selected_tags = []
    print(request.data["tags"])
    for tag in request.data["tags"]:
        temp = Tag.objects.filter(name=tag["name"])
        selected_tags.append(temp.get())
    user.tags.set(selected_tags)
    res = {"status": True, "message": "Successfully registered"}
    return response.Response(res, status.HTTP_201_CREATED)


@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def company_registration(request):
    serializer = CompanyCreateSerializer(data=request.data)
    if not serializer.is_valid(raise_exception=True):
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    user = serializer.save()
    res = {"status": True, "message": "Successfully registered"}
    return response.Response(res, status.HTTP_201_CREATED)
