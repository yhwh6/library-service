from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path(
        "admin/",
        admin.site.urls
    ),
    path(
        "users/",
        include("users.urls", namespace="users")
    ),
    path(
        "books/",
        include("books.urls", namespace="books")
    ),
    path(
        "borrowings/",
        include("borrowings.urls", namespace="borrowings")
    ),
    path(
        "schema/",
        SpectacularAPIView.as_view(),
        name="schema",
    ),
    path(
        "schema/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "__debug__/",
        include("debug_toolbar.urls")
    ),
]
