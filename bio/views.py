from django.shortcuts import render
from django.views import View
from django.db.models import Q
#For models queries
from .models import *
#from .models import Literature
# Create your views here.

class ArtPortfolio(View):
    def get(self, request, *args, **kwargs):

        art = Artwork.objects.all()

        context = {
            'art':art,
        }

        return render(request, 'bio/artpf.html', context)
    
#02/21/25


class AutoBio(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'bio/about.html')

class Home(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'bio/home.html')

class TDCPortfolio(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'bio/tdcpf.html')

class Library(View):
    def get(self, request, *args, **kwargs):

        novels = Literature.objects.filter(category__contains='Novel')
        comics = Literature.objects.filter(category__contains='Comic Book')
        magazines = Literature.objects.filter(category__contains='Magazine')
        flyers = Literature.objects.filter(category__contains='Flyer')

        context = {
            'novels' : novels, 
            'comics' : comics,
            'magazines' : magazines,
            'flyers' : flyers,
        }

        return render(request, 'bio/library.html', context)

class Read(View):
    def get(self, request, pk, *args, **kwargs):
        lit = Literature.objects.get(pk=pk)
        context = {
            'lit' : lit,
        }

        return render(request, 'bio/read.html', context)

class Info(View):
    def get(self, request, pk, *args, **kwargs):
        info = Artwork.objects.get(pk=pk)
        context={'info':info,}

        return render(request, 'bio/info.html', context)

class Videos(View):
    def get(self, request, *args, **kwargs):
        vids=Visual.objects.all()
        context={'vids':vids,}

        return render(request, 'bio/videos.html', context)