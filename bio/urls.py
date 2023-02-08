from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from bio.views import ArtPortfolio, AutoBio, TDCPortfolio, Library, Read, Info, Home


urlpatterns = [
    path('artpf/', ArtPortfolio.as_view(), name='artpf'),
    path('tdcpf/', TDCPortfolio.as_view(), name='tdcpf'),
    path('about/', AutoBio.as_view(), name='about'),
    path('', Home.as_view(), name="home"),
    path('library/', Library.as_view(), name='library'),
    #View specific item
    path('library/<int:pk>/', Read.as_view(), name='read'),
    path('artpf/<int:pk>/', Info.as_view(), name='info'),
] 