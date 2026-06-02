# accounts/serializers.py

from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        required=True
    )

    password_confirm = serializers.CharField(
        write_only=True,
        required=True
    )

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password",
            "password_confirm",
        )

    def validate(self, attrs):
        password = attrs.get("password")
        password_confirm = attrs.get("password_confirm")

        if password != password_confirm:
            raise serializers.ValidationError(
                {"password": "Les mots de passe ne correspondent pas."}
            )

        return attrs

    def create(self, validated_data):
        validated_data.pop("password_confirm")

        user = User.objects.create_user(
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
        )

        return user

# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(
#         write_only=True,
#         min_length=8
#     )
#
#     password_confirm = serializers.CharField(
#         write_only=True
#     )
#
#     class Meta:
#         model = User
#         fields = (
#             "first_name",
#             "last_name",
#             "email",
#             "password",
#             "password_confirm",
#         )
#
#     def validate(self, attrs):
#         if attrs["password"] != attrs["password_confirm"]:
#             raise serializers.ValidationError(
#                 {"password": "Les mots de passe ne correspondent pas."}
#             )
#
#         return attrs
#
#     def create(self, validated_data):
#         validated_data.pop("password_confirm")
#
#         user = User.objects.create_user(
#             email=validated_data["email"],
#             password=validated_data["password"],
#             first_name=validated_data["first_name"],
#             last_name=validated_data["last_name"],
#         )
#
#         return user

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "role",
            "avatar",
            "bio",
            "is_verified",
            "created_at",
        )

        read_only_fields = (
            "id",
            "role",
            "is_verified",
            "created_at",
        )

