from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from movies.models import Movie, Category, Actor, Genre
from movies.forms import ReviewFrom


class GenreYear:

    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values('year')


class MovieView(GenreYear, ListView):
    '''Вывод всех фильмов'''
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetail(GenreYear, DetailView):
    '''Вывод информации о фильме'''
    model = Movie
    slug_field = 'url'


class AddReview(View):
    '''Отзывы'''
    def post(self, request, pk):
        form = ReviewFrom(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())


class ActorView(GenreYear, DetailView):
    '''Вывод информации о актере'''
    model = Actor
    template_name = 'movies/actor.html'
    slug_field = 'name'


class FilterMoviesView(GenreYear ,ListView):
    '''Фильтр фильмов'''
    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist('year'))|
            Q(genres__in=self.request.GET.getlist('genre'))
            )
        return queryset


class JsonFilterMoviesView(ListView):
    """Фильтр фильмов в json"""
    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) |
            Q(genres__in=self.request.GET.getlist("genre"))
        ).distinct().values("title", "tagline", "url", "poster")
        # .distinct - не позволяет повторяться фильмам
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({"movies": queryset}, safe=False)
