from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .models import Movie
from users.models import User
from .serializers import MovieSerializer, MovieOrderSerializer
from rest_framework.views import Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from users.permissions import IsAdminOrReadOnly
# Create your views here.
class MovieView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request: Request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def post(self, request: Request):
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.check_object_permissions(request, serializer.validated_data)
        serializer.save(user=request.user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status.HTTP_201_CREATED)
    
class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request: Request, movie_id: int):
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer = MovieSerializer(movie)

        return Response(serializer.data, status.HTTP_200_OK)
        ...
    
    def delete(self, request: Request, movie_id: int):
        movie = get_object_or_404(Movie, id=movie_id)
        self.check_object_permissions(request, movie)
        movie.delete() 
        return Response(status=status.HTTP_204_NO_CONTENT)
        ...
    ...

class MovieOrderView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request: Request, movie_id: int):
        movie = get_object_or_404(Movie, id=movie_id)
        user = get_object_or_404(User, id=request.user.id)
        self.check_object_permissions(request, movie)

        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user, movie=movie)
        return Response(serializer.data, status.HTTP_201_CREATED)
    ...