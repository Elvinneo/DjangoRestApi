from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Movies
from.forms import MoviesForm


def movies_view(request):
    movies = Movies.objects.all()
    return render(request,'movies.html', {'movies': movies})


def api_view(request):
    return render(request,'withapi.html')
    
def add__movie__view(request):
    form=MoviesForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        movie=form.save(commit=False)
        movie.save()
        messages.success(request,"Film qeyd edildi ")
        return redirect("movies")
    return render(request,'addmovie.html', {'form': form})

