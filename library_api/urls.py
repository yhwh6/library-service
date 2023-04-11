from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path("books/", include("books.urls", namespace="books")),
    path("borrowings/", include("borrowings.urls", namespace="borrowings")),
    path("__debug__/", include("debug_toolbar.urls")),
]
