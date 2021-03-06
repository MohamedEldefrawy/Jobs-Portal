from account.models import User
from rest_framework import serializers


class DeveloperCreateSerialize(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})
    confirm_password = serializers.CharField(style={"input_type": "password"}, write_only=True,
                                             label="Confirm password")
    email = serializers.EmailField(required=True)
    date_of_birth = serializers.DateField(required=True)

    tags = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = User
        fields = ["email", "username", "password", "confirm_password",
                  "gender", "developer", "date_of_birth", "tags"]
        depth = 1

    def create(self, validated_data):
        email = validated_data["email"]
        username = validated_data["username"]
        password = validated_data["password"]
        confirm_password = validated_data["confirm_password"]
        gender = validated_data["gender"]
        developer = validated_data["developer"]
        date_of_birth = validated_data["date_of_birth"]
        if email and User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Email addresses must be unique."})
        if password != confirm_password:
            raise serializers.ValidationError({"password": "The two passwords differ."})
        user = User(email=email, gender=gender, date_of_birth=date_of_birth, developer=developer, username=username)
        user.set_password(password)
        user.save()
        return user


class CompanyCreateSerialize(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})
    confirm_password = serializers.CharField(style={"input_type": "password"}, write_only=True,
                                             label="Confirm password")

    class Meta:
        model = User
        fields = ["email", "password", "confirm_password", "company", "address", "history", "username"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        email = validated_data["email"]
        username = validated_data["username"]
        password = validated_data["password"]
        confirm_password = validated_data["confirm_password"]
        company = validated_data["company"]
        address = validated_data["address"]
        history = validated_data["history"]
        if email and User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Email addresses must be unique."})
        if password != confirm_password:
            raise serializers.ValidationError({"password": "The two passwords differ."})
        user = User(email=email, company=company, address=address, history=history, username=username)
        user.set_password(password)
        user.save()
        return user


class UserLoginSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "developer", "company"]


class DeveloperRetrieveSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "gender", "developer", "company", "date_of_birth", "tags", "cv"]
        depth = 1


class CompanyRetrieveSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "username", "address", "history", "company", "developer"]
        depth = 1
