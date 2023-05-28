from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """ Проверяет, имеет ли пользователь, отправивший запрос,
    права на доступ.
    Пользователям с ролью "admin" или атрибутом
    is_staff разрешены любые запросы.
    """
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or (
                request.user
                and request.user.is_authenticated
                and (request.user.role == "admin" or request.user.is_staff)
            )
        )


class IsAdminOrAuthor(permissions.BasePermission):
    """
        Проверяет, имеет ли пользователь, отправивший запрос,
        права на доступ к объекту или представлению.
        Разрешает запросы только на чтение (GET, HEAD, OPTIONS)
        пользователям с любыми правами доступа.
    """
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or (
                request.user
                and request.user.is_authenticated
            )
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or (
                request.user
                and (
                    (
                        request.user.role in ("admin", "moderator")
                        or request.user.is_staff
                    )
                    or obj.author == request.user
                )
            )
        )


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
            and (request.user.role == "admin" or request.user.is_staff)
        )
