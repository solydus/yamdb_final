from rest_framework import permissions
from .serializers import ADMIN_ROLE


class IsAdmin(permissions.BasePermission):
    """
        Проверяет, имеет ли пользователь, отправивший запрос,
        права на доступ к объекту или представлению.
        Разрешает запросы только на чтение (GET, HEAD, OPTIONS)
        пользователям с любыми правами доступа.
    """
    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and (request.user.role == ADMIN_ROLE or request.user.is_staff)
        )
