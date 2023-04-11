from borrowings.views import BorrowingViewSet

from django.urls import path, include

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"", BorrowingViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "borrowings"
