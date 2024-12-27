from django import forms
from .models import SeriesMovie

class SeriesMovieForm(forms.ModelForm):
    class Meta:
        model = SeriesMovie
        fields = ['title', 'description', 'genre', 'release_date', 'image']