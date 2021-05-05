from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Hero


# Create your views here.


def index(request):
    all_heroes = Hero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request, 'heroes/index.html', context)


def detail(request, hero_id):
    hero = Hero.objects.get(pk=hero_id)
    context = {
        'hero': hero
    }
    return render(request, 'heroes/detail.html', context)


def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catchphrase = request.POST.get('catchphrase')
        new_hero = Hero(name=name, alter_ego=alter_ego, primary_ability=primary_ability, secondary_ability=secondary_ability, catchphrase=catchphrase)
        new_hero.save()
        return HttpResponseRedirect(reverse('hero_app:index'))
    else:
        return render(request, 'heroes/create.html')
