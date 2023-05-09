"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

# from women.views import WomenAPIList, WomenAPIUpdate, WomenAPIDetailView
from women.views import WomenAPIList, WomenAPIUpdate, WomenAPIDestroy
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from rest_framework import routers

# Маршрутизаторы в DRF
# Маршрутизация ресурсов позволяет быстро объявить все общие маршруты для данного ресурсного контроллера.
# Вместо того чтобы объявлять отдельные маршруты для вашего индекса… ресурсный маршрут объявляет их в одной строке кода
# Фреймворк REST добавляет в Django поддержку автоматической маршрутизации URL и предоставляет вам простой,
# быстрый и последовательный способ подключения логики представления к набору URL.
# https://django.fun/ru/docs/django-rest-framework/3.12/api-guide/routers/

# Можно создавать собственные роутеры
class MyCustomRouter(routers.SimpleRouter):
    routes = [
        # Каждый класс определяет 1 маршрут
        routers.Route(url=r'^{prefix}$',              # Шаблон маршрута
                      mapping={'get': 'list'},        # Связывает тип запроса с соотв. методом ViewSet
                      name='{basename}-list',         # Название маршрута
                      detail=False,                   # Список или запись
                      initkwargs={'suffix': 'List'}   # Доп аргументы
                      ),
        routers.Route(url=r'^{prefix}/{lookup}$',
                      mapping={'get': 'retrieve'},
                      name='{basename}-detail',
                      detail=True,
                      initkwargs={'suffix': 'Detail'}
                      )
    ]

# from rest_framework import routers
#
# router = routers.SimpleRouter()
# # Регистрируем в роутере WomenViewSet, r'...' - префикс для набора маршрута
# router.register(r'women', WomenViewSet, basename='women')
# print(router.urls)


urlpatterns = [
    path('admin/', admin.site.urls),

    # Подключаем авторизацию через сессию
    # https://django.fun/ru/docs/django-rest-framework/3.12/api-guide/authentication/
    path('api/v1/drf-auth/', include('rest_framework.urls')),

    # path('api/v1/', include(router.urls)),  # http://127.0.0.1:8000/api/v1/women/

    # # Указываем метод для обработки запроса (get) и метод который будет вызываться в самом ViewSet
    # # для обработки (get) запроса, в нашем случае метод .list()
    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),
    # # Когда в маршруте будем указывать рк-записи, обрабатывать будем (put) запрос, а обрабатывать
    # # (put) запрос будет метод .update()
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),

    # v1 - версия сериализатора
    path('api/v1/women/', WomenAPIList.as_view()),
    # Передаём рк записи которую хотим поменять
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),

    # Пути  Djoser
    # https://djoser.readthedocs.io/en/latest/base_endpoints.html
    path('api/v1/auth/', include('djoser.urls')),  # new
    # Путь ваторизации по токенам
    re_path(r'auth/', include('djoser.urls.authtoken')),  # new

    # Simplt JWT
    # https://django-rest-framework-simplejwt.readthedocs.io/en/latest/
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Декодирование JWT токенов https://jwt.io/
]
