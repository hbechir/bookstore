from django import forms
from .models import Author, Book

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'surname']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors']
