from django.shortcuts import render
from .models import Game
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse('hello')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', { 'games': games })

def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'games/detail.html', {'game' : game})