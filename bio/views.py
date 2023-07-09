from django.shortcuts import render
from django.views import View
#For models queries
from .models import *
#from .models import Literature
# Create your views here.

class ArtPortfolio(View):
    def get(self, request, *args, **kwargs):

        art = Artwork.objects.all()
        sps = Artwork.objects.filter(entry__contains='Self-Portraits')
        chs = Artwork.objects.filter(entry__contains='Characters')
        sks = Artwork.objects.filter(entry__contains='Sketches')
        mms = Artwork.objects.filter(entry__contains='Mixed-Media')
        has = Artwork.objects.filter(entry__contains='Hatching')
        pos = Artwork.objects.filter(entry__contains='Portraits')
        ips = Artwork.objects.filter(entry__contains='Imagined Portaits')

        context = {
            'art':art,
            'sps':sps,
            'chs':chs,
            'sks':sks,
            'mms':mms,
            'has':has,
            'pos':pos,
            'ips':ips,
        }

        return render(request, 'bio/artpf.html', context)

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