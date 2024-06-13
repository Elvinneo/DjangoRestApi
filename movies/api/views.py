from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from .serializers import MovieSerializer
from ..models import Movies


class MoviesListAPIView(ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer


class MoviesDetailAPIView(RetrieveAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    lookup_field = "pk"


class MoviesDeleteAPIView(DestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    lookup_field = "pk"


class MoviesUpdateAPIView(UpdateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
    lookup_field = "pk"

