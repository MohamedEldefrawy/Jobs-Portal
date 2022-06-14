# Create your views here.
import datetime

import jwt
from account.models import User
from rest_framework import permissions, decorators, response, status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from tag.models import Tag

from .serializers import DeveloperCreateSerialize, CompanyCreateSerialize, DeveloperRetrieveSerialize, \
    UserLoginSerialize, CompanyRetrieveSerialize


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


@decorators.api_view(["POST"])
def login(request):
    email = request.data["email"]
    password = request.data["password"]
    selected_user = User.objects.filter(email=email).first()
    if selected_user is None:
        raise AuthenticationFailed('User not found')
    if not selected_user.check_password(password):
        raise AuthenticationFailed('Incorrect password')

    payload = {
        "id": selected_user.id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        "lat": str(datetime.datetime.utcnow()),
    }

    token = jwt.encode(payload, 'secret', algorithm='HS256')
    res = Response()
    res.set_cookie(key="JWT", value=token, httponly=True)
    res.data = {
        "status": True,
        "message": "Login Success",
        "token": token
    }
    return res


@decorators.api_view(["GET"])
def view_user(request):
    token = request.COOKIES.get("JWT")
    if not token:
        raise AuthenticationFailed("Unauthenticated")
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Unauthenticated")
    user = User.objects.filter(id=payload['id']).first()
    if user.developer:
        serializer = UserLoginSerialize(user)
    else:
        serializer = UserLoginSerialize(user)
    return Response(serializer.data)


@decorators.api_view(["GET", "PUT"])
def user(request, pk):
    selected_user = User.objects.filter(pk=pk).first()
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
