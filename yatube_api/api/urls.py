from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CommentViewSet, FollowListCreateAPIView, GroupViewSet,
                    PostViewSet)

app_name = "api"

v1_router = DefaultRouter()
v1_router.register(r"posts", PostViewSet)
v1_router.register(r"groups", GroupViewSet)
v1_router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comment"
)

urlpatterns = [
    path("v1/follow/", FollowListCreateAPIView.as_view()),
    path("v1/", include(v1_router.urls)),
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
]
