from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from contest.models import Album

class AlbumIndexView(ListView):
    model = Album
    template_name = 'contest/panel/album/index.html'

class AlbumCreateView(CreateView):
    model = Album
    fields = ['album_name', 'author']
    template_name = 'contest/panel/album/create.html'
    success_url = reverse_lazy('panel:albums:index')

class AlbumUpdateView(UpdateView):
    model = Album
    fields = ['album_name', 'author']
    template_name = 'contest/panel/album/edit.html'
    success_url = reverse_lazy('panel:albums:index')

class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'contest/panel/album/delete.html'
    success_url = reverse_lazy('panel:albums:index')