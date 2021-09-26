from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import GroupViewSet, PostViewSet, CommentViewSet

router_v1 = DefaultRouter()
router_v1.register(r'v1/posts', PostViewSet, basename='posts_v1')
router_v1.register(r'v1/posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comments_v1')
router_v1.register(r'v1/groups', GroupViewSet, basename='group_v1')

urlpatterns = [
    path(r'', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
