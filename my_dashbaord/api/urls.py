from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserView, UsersListView

router = DefaultRouter()
router.register(r"Users", UserView)
router.register(r"Users-list", UsersListView)

urlpatterns = [path("api/", include(router.urls))]
