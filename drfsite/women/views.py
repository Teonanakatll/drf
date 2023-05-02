from django.forms import model_to_dict
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer


# Класс APIView стоит во главе иерархии всех классов представлений в drf
# сайт www.django-rest-framework.org/api-guide/generic-views/
class WomenAPIView(APIView):
    # Метод get отвечает за обработку всех get-запросов на сервер
    def get(self, request):  # request хранит все параметры входящего get-запроса
        w = Women.objects.all()
        # Response преобразовывает словарь в байтовую djson строку
        # Параметр many=True говарит о том что сериализатор должен обработывать список записей
        # и выдавать список записей, абращаемся к коллекции data которя будет представлять собой
        # словарь преобразованных данных из коллекции Women.
        return Response({'posts': WomenSerializer(w, many=True).data})

    # Метод post служит для добавления записей в бд
    def post(self, request):
        # Создаём обьект сериализатора с данными переданными в запросе
        serializer = WomenSerializer(data=request.data)
        # Проверяем данные на валидность и в случае не соответствия вызываем исключение
        # в виде json-строки.
        serializer.is_valid(raise_exception=True)
        # Создадим переменную которая будет ссылаться на новую (добавленную) запись в таблицу Women
        post_new = Women.objects.create(
            # Передаём методу create аргументы из коллекции (словаря) request.data[], отправленные в post запросе
            title=request.data['title'],
            content=request.data['content'],
            cat_id=request.data['cat_id']
        )
        # В ответ отправляем пользователю значения новой (добваленной) записи
        # Функция model_to_dict() преобразовывает модель джанга в словарь
        # return Response({'post': model_to_dict(post_new)})
        return Response({'post': WomenSerializer(post_new).data})

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

