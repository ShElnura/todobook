from django import forms
from webapp.models import Book


class BookAddForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'subtitle', 'description', 'price', 'genre', 'author', 'year')
