from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from rest_framework import generics
from .serializers import *
from .permissions import *
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwnerOrReadOnly
from .forms import *
from django.contrib.auth import login, logout

def addstar(request):
    if request.method == 'POST':
        star = Rating(request.POST)
        stars = []
        stars += star
        messages.success(request, 'Вы успешно отправили отзыв', star) 


class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer


class CategoryUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryDestroyView(generics.DestroyAPIView):
    serializer_class = CategorySerializer


class ActorCreateView(generics.CreateAPIView):
    serializer_class = ActorSerializer


class ActorUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()

class ActorGenericView(generics.GenericAPIView):
    serializer_class = ActorSerializer


class ActorListView(generics.ListAPIView):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()

class ActorDestroyView(generics.DestroyAPIView):
    serializer_class = ActorSerializer


class MovieCreateView(generics.CreateAPIView):
    serializer_class = MovieSerializer

class MovieUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

class MovieGenericView(generics.GenericAPIView):
    serializer_class = MovieSerializer


class MovieListView(generics.ListAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

class MovieDestroyView(generics.DestroyAPIView):
    serializers_class = MovieSerializer

class GenreCreateView(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializers_class = GenreSerializer

class GenreUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializers_class = GenreSerializer
    queryset = Genre.objects.all()

class GenreGenericView(generics.GenericAPIView):
    serializer_class = GenreSerializer


class GenreListView(generics.ListAPIView):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

class GenreDestroyView(generics.DestroyAPIView):
    serializer_class = GenreSerializer



class RatingCreateView(generics.CreateAPIView):
    serializer_class = RatingSerializer


class RatingUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

class RatingGenericView(generics.GenericAPIView):
    serializer_class = RatingSerializer


class RatingListView(generics.ListAPIView):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()

class RatingDestroyView(generics.DestroyAPIView):
    serializer_class = RatingSerializer



class MovieImageCreateView(generics.CreateAPIView):
    serializer_class = MovieImageSerializer
   

class MovieImageUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieImageSerializer
    queryset = MovieImage.objects.all()

class MovieImageGenericView(generics.GenericAPIView):
    serializer_class = MovieImageSerializer


class MovieImageListView(generics.ListAPIView):
    serializer_class = MovieImageSerializer
    queryset = MovieImage.objects.all()

class MovieImageDestroyView(generics.DestroyAPIView):
    serializer_class = MovieImageSerializer



class ReviewCreateView(generics.CreateAPIView):
    serializer_class = ReviewSerializer


class ReviewUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

class ReviewGenericView(generics.GenericAPIView):
    serializer_class = ReviewSerializer


class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

class ReviewDestroyView(generics.DestroyAPIView):
    serializer_class = ReviewSerializer




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'blog/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'blog/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')
