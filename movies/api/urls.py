from django.urls import path
from .views import (
    MoviesListAPIView,
    MoviesDetailAPIView,
    MoviesUpdateAPIView,
    MoviesDeleteAPIView,
)

urlpatterns = [
    path("list/", MoviesListAPIView.as_view(), name="api-list"),
    path("detail/<pk>", MoviesDetailAPIView.as_view(), name="api-detail"),
    path("update/<pk>", MoviesUpdateAPIView.as_view(), name="api-update"),
    path("delete/<pk>", MoviesDeleteAPIView.as_view(), name="api-delete"),
]