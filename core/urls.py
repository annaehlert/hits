"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from telnetlib import LOGOUT

from django.contrib import admin
from django.urls import path, include

from contest.views.generic_views import (
    AlbumIndexView,
    AlbumCreateView,
    AlbumUpdateView,
    AlbumDeleteView
)
from contest.views.standard_views import (
    CommonIndexView,
    PanelIndexView,
    AuthorIndexView,
    AuthorCreateView,
    AuthorDeleteView,
    AuthorUpdateView, SongIndexView, SongCreateView, SongEditView, SongDeleteView, LoginView, logout_view
)

album_patterns = ([
    path('', AlbumIndexView.as_view(), name="index"),
    path('create/', AlbumCreateView.as_view(), name="create"),
    path('<int:pk>/edit/', AlbumUpdateView.as_view(), name="edit"),
    path('<int:pk>/delete/', AlbumDeleteView.as_view(), name="delete"),
    path('<int:album_id>/songs/', SongIndexView.as_view(), name="songs-index"),
    path('<int:album_id>/songs/create', SongCreateView.as_view(), name="songs-create"),
    path('<int:album_id>/songs/<int:song_id>/edit', SongEditView.as_view(), name="songs-edit"),
    path('<int:album_id>/songs/<int:song_id>/delete', SongDeleteView.as_view(), name="songs-delete"),
], 'albums')

author_patterns = ([
    path('', AuthorIndexView.as_view(), name="index"),
    path('create/', AuthorCreateView.as_view(), name="create"),
    path('<int:id>/delete/', AuthorDeleteView.as_view(), name="delete"),
    path('<int:id>/edit/', AuthorUpdateView.as_view(), name="edit"),
    ], 'authors')

panel_patterns = ([
    path('', PanelIndexView.as_view(), name='index'),
    path('authors/', include(author_patterns)),
    path('albums/', include(album_patterns))
],  'panel')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CommonIndexView.as_view(), name='common-index'),
    path('panel/', include(panel_patterns)),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout')
]
