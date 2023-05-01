from rest_framework import serializers
from .models import Women

# Сериалайзер который работает с моделями, будет брать данные модели из бд,
# представлять их в json-формате и отправлять их в ответ на запрос пользователя


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ('title', 'cat_id')
