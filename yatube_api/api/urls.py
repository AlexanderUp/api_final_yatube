from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = "api"

v1_router = DefaultRouter()
v1_router.register(r"posts", PostViewSet)
v1_router.register(
    r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comment"
)
v1_router.register(r"groups", GroupViewSet)
v1_router.register(r"follow", FollowViewSet, basename="follow")

urlpatterns = [
    path("v1/", include(v1_router.urls)),
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
]
