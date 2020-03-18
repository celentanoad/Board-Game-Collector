from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import uuid
import boto3
from .models import Game, Store, Photo
from django.http import HttpResponse
# Create your views here.

#below added when including photo upload:
S3_BASE_URL = 'https://s3-us-east-2.amazonaws.com/'
BUCKET = 'boardgamecollector'

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

def add_photo(request, game_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, game_id=game_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', game_id=game_id)