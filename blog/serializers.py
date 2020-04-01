from rest_framework import serializers

class CreateArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=32)


class UpdateArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=32, required=False)


class DeleteArticleSerializer(serializers.Serializer):
    pass
