from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    # Переопределяем метод has_permissions на уровне всего запроса
    def has_permission(self, request, view):
        # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS') - запросы тлько для чтения (безопасные)
        if request.method in permissions.SAFE_METHODS:
            # Предостовляем доступ
            return True
        # а иначе только для администратора
        return bool(request.user and request.user.is_staff)

class IsOwnerOrReadOnly(permissions.BasePermission):
    # Разрешение на уровне обьекта, для конкретной записи
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        # Если user из записи в бд тот же что и пришел с запросом возвращаем True (даём доступ)
        return obj.user == request.user
