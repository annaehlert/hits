from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from contest.forms.standard_forms import AuthorForm, LoginForm
from contest.models import Author, Song, Album
from contest.forms.model_forms import SongForm


class LoginView(View):
    def get(self, request):
        if request.user.id is not None:
            return redirect('panel:index')

        return render(
            request,
            "contest/auth/login.html",
        {"form": LoginForm()}
        )
    def post(self, request):
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(
                request,
                "contest/auth/login.html",
                {"form": form}
            )
        user = authenticate(
            request=request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user is None:
            messages.add_message(request, messages.WARNING, 'User does not exist')
            return redirect('login')
        login(request, user)
        messages.add_message(request,messages.SUCCESS, 'User logged in successfully')#wytworzenie pliku sesji i cookies
        return redirect('panel:index')


@login_required
def logout_view(request):
    logout(request)
    return redirect('common-index')


class CommonIndexView(View):
    def get(self, request):
        return render(request, "contest/common/index.html",
                      {"songs": Song.objects.all().order_by('sort_order')}
                      )


class PanelIndexView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "contest/panel/index.html")


class AuthorIndexView(LoginRequiredMixin, View):
    def get(self, request):
        authors = Author.objects.all().order_by('band_name')
        return render(request, "contest/panel/author/index.html", {
            "authors": authors
        })

class AuthorCreateView(LoginRequiredMixin, View):

    def get(self, request):
        return render(request,
                      "contest/panel/author/create.html", {
            "form": AuthorForm()}
                      )

    def post(self, request):
        form = AuthorForm(request.POST)
        if not form.is_valid():
            return render(
                request,
                "contest/panel/author/create.html",
                {"form": form}
            )
        Author.objects.create(
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            band_name=form.cleaned_data['band_name'],
            birth_date=form.cleaned_data['birth_date'],
            debut=form.cleaned_data['debut'])
        return redirect('panel:authors:index')
            # if Author.objects.filter(name=band_name).exists():
            #     return render(request, "contest/panel/author/index.html", {
            #         "form": form,
            #         "to_be_add_2": to_be_add_2
            #     })

class AuthorDeleteView(LoginRequiredMixin, View):

    def get(self, request, id):
        author = Author.objects.get(id=id)
        author.delete()
        return redirect('panel:authors:index')

class AuthorUpdateView(LoginRequiredMixin, View):
    def get(self, request, id):
        author = Author.objects.get(id=id)
        form = AuthorForm({
            "first_name": author.first_name,
            "last_name": author.last_name,
            "band_name": author.band_name,
            "birth_date": author.birth_date,
            "debut": author.debut
        })
        return render(request, "contest/panel/author/edit.html", {
            "form": form,
            "author": author
        })

    def post(self, request, id):
        author = Author.objects.get(id=id)
        form = AuthorForm(request.POST)
        if not form.is_valid():
            return render(request, "contest/panel/author/edit.html", {
                "form": form,
                "author": author
            })

        author.first_name = form.cleaned_data['first_name']
        author.last_name = form.cleaned_data['last_name']
        author.band_name = form.cleaned_data['band_name']
        author.birth_date = form.cleaned_data['birth_date']
        author.debut = form.cleaned_data['debut']
        author.save()
        return redirect('panel:authors:index')


class SongIndexView(LoginRequiredMixin, View):
    def get(self, request, album_id):
        songs = Song.objects.filter(album_id=album_id)
        album = Album.objects.get(id=album_id)
        return render(request, "contest/panel/song/index.html", {
            "songs": songs,
            "album": album
        })

class SongCreateView(LoginRequiredMixin, View):
    def get(self, request, album_id):
        form = SongForm()
        album = Album.objects.get(id=album_id)
        return render(request, "contest/panel/song/create.html", {
            "form": form,
            "album": album
        })

    def post(self, request, album_id):
        form = SongForm(request.POST)
        album = Album.objects.get(id=album_id)
        if not form.is_valid():
            return render(request, "contest/panel/song/create.html", {
                "form": form,
                "album": album
            })
        new_song = form.save(commit=False)
        new_song.album_id = album_id
        new_song.save()
        return redirect('panel:albums:songs-index', album_id=album_id)

class SongEditView(LoginRequiredMixin, View):
    def get(self, request, album_id, song_id):
        song = Song.objects.get(id=song_id)
        album = Album.objects.get(id=album_id)
        form = SongForm(instance=song)
        return render(request, "contest/panel/song/edit.html", {
            "form": form,
            "album": album,
            "song": song
        })

    def post(self, request, album_id, song_id):

        song = Song.objects.get(pk=song_id)
        album = Album.objects.get(id=album_id)
        form = SongForm(request.POST, instance=song)
        if not form.is_valid():
            return render(request, "contest/panel/song/edit.html", {
                "form": form,
                "album": album,
                "song" : song
            })
        form.save()
        return redirect('panel:albums:songs-index', album_id=album_id)


class SongDeleteView(LoginRequiredMixin, View):
    def get(self, request, album_id, song_id):
        song = Song.objects.get(id=song_id)
        if song:
            song.delete()
        return redirect('panel:albums:songs-index', album_id=album_id)



