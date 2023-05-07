from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Women
from .serializers import WomenSerializer

# ViewSet - позволяет объединить логику для набора связанных представлений в одном классе
# https://django.fun/ru/docs/django-rest-framework/3.12/api-guide/viewsets/

# ModelViewSet - действия, предоставляемые классом ModelViewSet: .list() , .retrieve() ,
# .create() , .update() ,.partial_update() , и .destroy().

# Класс APIView стоит во главе иерархии всех классов представлений в drf
# сайт www.django-rest-framework.org/api-guide/generic-views/


class WomenViewSet(viewsets.ModelViewSet):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


# # ListCreateAPIView реализует 2 метода (get() и post())
# class WomenAPIList(generics.ListCreateAPIView):
#     # Создаём queryset который будет ссылаться на список записей который мы будем возвращать клиенту.
#     queryset = Women.objects.all()
#     # Сериализатор который будет обрабатывать queryset
#     serializer_class = WomenSerializer
#
# # UpdateAPIView выполняет put() и patch() запросы (изменяет записи)
# class WomenAPIUpdate(generics.UpdateAPIView):
#     # Связываем queryset с моделью Women (ленивый запрос), класс UpdateAPIView обработает
#     # queryset и вернёт только одну изменённую запись.
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
# # RetrieveUpdateDestroyAPIView - получить, изменить, удалить запись. (get(), pyt(), patch(), delete())
# class WomenAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


# class WomenAPIView(APIView):
#     # Метод get отвечает за обработку всех get-запросов на сервер
#     def get(self, request):  # request хранит все параметры входящего get-запроса
#         w = Women.objects.all()
#         # Response преобразовывает словарь в байтовую djson строку
#         # Параметр many=True говарит о том что сериализатор должен обработывать список записей
#         # и выдавать список записей, абращаемся к коллекции data которя будет представлять собой
#         # словарь преобразованных данных из коллекции Women.
#         return Response({'posts': WomenSerializer(w, many=True).data})
#
#     # Метод post служит для добавления записей в бд
#     def post(self, request):
#         # Создаём обьект сериализатора с данными переданными в запросе
#         serializer = WomenSerializer(data=request.data)
#         # Проверяем данные на валидность и в случае не соответствия вызываем исключение
#         # в виде json-строки.
#         # После проверки валидации появится коллекция validated_data, результат декодирования json-строки
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         # Определяем pk записи которую нужно изменить
#         pk = kwargs.get("pk", None)
#         # Если в запросе не существует pk отправляем клиенту сообщение
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Women.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})

    #     # Если мы получили и ключ и запись по этому ключу, создаём обьект сериализатор с аргументами
    #     # request.data (данные которые мы хотим изменить) и обьект instance (запись которую мы будем менять)
    #     serializer = WomenSerializer(data=request.data, instance=instance)
    #     # В обьекте serializer проверяем принятые данные
    #     # После проверки валидации появится коллекция validated_data, результат декодирования json-строки
    #     serializer.is_valid(raise_exception=True)
    #     # Так как в сериализатор мы передаём аргументы data и instance при вызаве метода save() отработает
    #     # функция update()
    #     serializer.save()
    #     # Клиенту отправляем запрос в виде json-строки
    #     return Response({"post": serializer.data})
    #
    # def delete(self, request, *args, **kwargs):
    #     pk = kwargs.get("pk", None)
    #     if not pk:
    #         return Response({"error", "Method DELETE not allowed"})
    #
    #     item = Women.objects.get(pk=pk)
    #     item.delete()
    #
    #     return Response({"post": "delete post " + str(pk)})

        # #...! Это действие была для демонстрации работы сериалайзера, перенесено непосредственно в сериалайзер.
        # # Создадим переменную которая будет ссылаться на новую (добавленную) запись в таблицу Women
        # post_new = Women.objects.create(
        #     # Передаём методу create аргументы из коллекции (словаря) request.data[], отправленные в post запросе
        #     title=request.data['title'],
        #     content=request.data['content'],
        #     cat_id=request.data['cat_id']
        # )

        # В ответ отправляем пользователю значения новой (добваленной) записи
        # Функция model_to_dict() преобразовывает модель джанга в словарь
        # return Response({'post': model_to_dict(post_new)})
        # return Response({'post': WomenSerializer(post_new).data})


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

