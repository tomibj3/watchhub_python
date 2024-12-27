from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import SeriesMovie
from .forms import SeriesMovieForm

# Create your views here.

def home_view(request):
    series_movies = SeriesMovie.objects.all()
    return render(request, 'search/home.html', {'series_movies': series_movies})

def search_list(request):
    series_movies = SeriesMovie.objects.all()
    return render(request, 'search/search_list.html', {'series_movies': series_movies})

def search_detail(request, series_movie_id):
    series_movie = get_object_or_404(SeriesMovie, id=series_movie_id)
    return render(request, 'search/search_detail.html', {'series_movie': series_movie})

def about(request):
    return render(request, 'search/about.html')

@login_required
def add_series_movie(request):
    if request.method == 'POST':
        form = SeriesMovieForm(request.POST, request.FILES)
        if form.is_valid():
            series_movie = form.save(commit=False)
            series_movie.created_by = request.user
            series_movie.save()
            return redirect('search_list')
    else:
        form = SeriesMovieForm()
    return render(request, 'search/search_form.html', {'form': form})

@login_required
def delete_series_movie(request, series_movie_id):
    series_movie = get_object_or_404(SeriesMovie, id=series_movie_id)
    if request.method == 'POST':
        series_movie.delete()
        return redirect('home')
    return render(request, 'search/delete_confirmation.html', {'series_movie': series_movie})