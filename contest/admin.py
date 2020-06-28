from django.contrib import admin
from contest.models import SongVotes, ContestSubmission, Song


@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    pass


@admin.register(SongVotes)
class SongVotesAdmin(admin.ModelAdmin):
    pass


@admin.register(ContestSubmission)
class ContestSubmissionAdmin(admin.ModelAdmin):
    pass
