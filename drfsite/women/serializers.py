import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Women


# Сериалайзер который работает с моделями, будет брать данные модели из бд,
# представлять их в json-формате и отправлять их в ответ на запрос пользователя

# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    # read_only=True поля только для чтения, будем читать при добавлении в бд.
    time_create = serializers.DateTimeField(read_only=True)
    teme_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        # Передаём методу create() класса Women распакованные данные из post-запроса прошедшие валидацию
        return Women.objects.create(**validated_data)

    # instance ссылка на запись в бд, validated_data словарь из проверенных данных которые нужно изменить в бд
    def update(self, instance, validated_data):
        # Так как instance это обьект модели Women, то используя ORM джанго присваиваем полям instance зночения
        # полей из славаря validated_data, иначе (если неможем взять значение из славаря) прописываем значение которое
        # уже есть в этой модели Women
        instance.title = validated_data.get("title", instance.title)
        instance.content = validated_data.get("content", instance.content)
        instance.time_update = validated_data.get("time_update", instance.time_update)
        instance.is_published = validated_data.get("is_published", instance.is_published)
        instance.cat_id = validated_data.get("cat_id", instance.cat_id)
        instance.save()
        return instance

# ПРОПИСЫВАЕМ ФУНКЦИИ СЕРЕАЛИЗАТОРА ВРУЧНУЮ
# # Функция кодирования модели в json-строку
# def encode():
#     model = WomenModel('Angelina Jolie', 'Content: Angelina Jolie')
#     # Создаём обьект класса сериализатора, ередаём модель аргументом, получаем
#     # обьект сериализатора (словарь) из полей переданной модели
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     # Чтобы из обьекта сериализатора (словаря) получить json-строку, создаём обьект класса JSONRenderer()
#     # вызываем у него метод render() и передадим в него колекцию model_sr.data
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# # Функция декодирования json-строки в модель
# def decode():
#     stream = io.BytesIO(b'{"title":"Angelina Jolie","content":"Content: Angelina Jolie"}')
#     # Создаём обьект класса JSONParser(), в метод parse() передаём поток (stream)
#     data = JSONParser().parse(stream)
#     # Создаём обьект сериализатора и чтобы декодировать данные передаём именованный параметр data
#     serializer = WomenSerializer(data=data)
#     # Проверяем корректность переданных данных
#     serializer.is_valid()
#     # После проверки валидации появится коллекция validated_data, результат декодирования json-строки
#     print(serializer.validated_data)

# python manage.py shell
# from women.serislizers import (encode/decode)
# encode() decode()
