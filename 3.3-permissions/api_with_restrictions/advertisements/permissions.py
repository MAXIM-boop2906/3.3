from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """
    Обновлять и удалять объявление может только его автор.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешаем GET, HEAD, OPTIONS всем
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Для PUT, PATCH, DELETE — только автор
        return obj.creator == request.user


class IsAdminOrOwner(BasePermission):
    """
    Админы могут менять и удалять любые объявления.
    Обычные пользователи — только свои.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Админ может всё
        if request.user and request.user.is_staff:
            return True
        # Обычный пользователь — только свои объявления
        return obj.creator == request.user