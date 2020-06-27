from django import forms

from contest.models import Album, Song, SongVotes, ContestSubmission


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['author', 'album_name']


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['song_name', 'year', 'album', 'yt_link', 'sort_order']


class SongVotesForm(forms.ModelForm):
    class Meta:
        model = SongVotes
        fields = ['song', 'vote_hash']


class ContestSubmissionForm(forms.ModelForm):
    class Meta:
        model = ContestSubmission
        fields = ['song', 'first_name', 'last_name', 'telephone', 'email', 'context']
