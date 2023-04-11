from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import CreateUserView, ManageUserView

app_name = "users"

urlpatterns = [
    path(
        "create/",
        CreateUserView.as_view(),
        name="create",
    ),
    path(
        "token/",
        TokenObtainPairView.as_view(),
        name="token-obtain-pair",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(),
        name="token-refresh",
    ),
    path(
        "me/",
        ManageUserView.as_view(),
        name="manage",
    ),
]
