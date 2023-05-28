from django.urls import path, include
from rest_framework import routers

from .views import UserViewSet, UserCreateViewSet, UserReceiveTokenViewSet


router = routers.SimpleRouter()
router.register('', UserViewSet, basename='users')


user_urls = [
    path('', UserViewSet.as_view({'get': 'list'}), name='user-list'),
    path(
        '<int:pk>/',
        UserViewSet.as_view({'get': 'retrieve'}),
        name='user-detail'
    ),
    path(
        '<int:pk>/profile/',
        UserViewSet.as_view({'get': 'retrieve'}),
        name='profile'
    ),
    path(
        '<int:pk>/profile/edit/',
        UserViewSet.as_view({'patch': 'partial_update'}),
        name='profile-edit'
    ),
]

auth_urls = [
    path(
        'signup/',
        UserCreateViewSet.as_view({'post': 'create'}),
        name='signup'
    ),
    path(
        'token/',
        UserReceiveTokenViewSet.as_view({'post': 'create'}),
        name='token'
    )
]


urlpatterns = [
    path('api/v1/users/', include(router.urls)),
    path('api/v1/users/', include(user_urls)),
    path('api/v1/auth/', include(auth_urls)),
]
