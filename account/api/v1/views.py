from account.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
from rest_framework import permissions, decorators, response, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from tag.models import Tag

from .serializers import DeveloperCreateSerialize, CompanyCreateSerialize, DeveloperRetrieveSerialize, \
    UserLoginSerialize, CompanyRetrieveSerialize


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])
def register(request):
    if request.data['developer']:
        serializer = DeveloperCreateSerialize(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        selected_tags = []
        for tag in request.data["tags"]:
            temp = Tag.objects.filter(name=tag["name"])
            selected_tags.append(temp.get())
        user.tags.set(selected_tags)
        res = {"status": True, "message": "Successfully registered"}
        return response.Response(res, status.HTTP_201_CREATED)
    elif request.data['company']:
        serializer = CompanyCreateSerialize(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        res = {"status": True, "message": "Successfully registered"}
        return response.Response(res, status.HTTP_201_CREATED)
    else:
        return response.Response({"Message": "please select correct account type"}, status.HTTP_400_BAD_REQUEST)


@decorators.api_view(["GET"])
def view_user(request):
    user = Token.objects.get(key='token string').user
    if user.developer:
        serializer = UserLoginSerialize(user)
    else:
        serializer = UserLoginSerialize(user)
    return Response(serializer.data)


@decorators.api_view(["GET", "PUT"])
def user(request, user_id):
    selected_user = User.objects.filter(id=user_id).first()
    if request.method == "GET":
        if selected_user:
            if selected_user.developer:
                serializer = DeveloperRetrieveSerialize(selected_user)
                return Response(serializer.data, status.HTTP_200_OK)
            elif selected_user.company:
                serializer = CompanyRetrieveSerialize(selected_user)
                return Response(serializer.data, status.HTTP_200_OK)
        return Response({"message": "user is not found"}, status.HTTP_404_NOT_FOUND)
    elif request.method == "PUT":
        if selected_user:
            if selected_user.developer:
                serializer = DeveloperRetrieveSerialize(instance=selected_user, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                return Response(serializer.data, status.HTTP_200_OK)
            elif selected_user.company:
                serializer = CompanyRetrieveSerialize(instance=selected_user, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                return Response(serializer.data, status.HTTP_200_OK)
        return Response({"message": "user is not found"}, status.HTTP_404_NOT_FOUND)


@decorators.api_view(["POST"])
def logout(request):
    try:
        print(request.user)
        request.user.auth_token.delete()
    except (AttributeError, ObjectDoesNotExist):
        pass

    return Response({"success": _("Successfully logged out.")},
                    status=status.HTTP_200_OK)
