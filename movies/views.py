from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from movies.models import Movie, Category, Actor
from movies.forms import ReviewFrom


class MovieView(ListView):
    '''Вывод всех фильмов'''
    model = Movie
    queryset = Movie.objects.filter(draft=False)


class MovieDetail(DetailView):
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


class ActorView(DetailView):
    '''Вывод информации о актере'''
    model = Actor
    template_name = 'movies/actor.html'
    slug_field = 'name'
