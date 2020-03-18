from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game, Store
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', { 'games': games })

def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    stores_not_in_list = Store.objects.exclude(id__in = game.stores.all().values_list('id'))
    return render(request, 'games/detail.html', {'game' : game, 'stores': stores_not_in_list})

class GameCreate(CreateView):
    model = Game
    fields = '__all__'

class GameUpdate(UpdateView):
    model = Game
    fields = ['numPlayers', 'description']

class GameDelete(DeleteView):
    model = Game
    success_url = '/games/'

def assoc_store(request, game_id, store_id):
    Game.objects.get(id=game_id).stores.add(store_id)
    return redirect('detail', game_id=game_id)

def unassoc_store(request, game_id, store_id):
    Game.objects.get(id=game_id).stores.remove(store_id)
    return redirect('detail', game_id=game_id)