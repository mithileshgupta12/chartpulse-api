from rest_framework import serializers

class PostLoginValidator(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)