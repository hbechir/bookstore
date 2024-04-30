from django.shortcuts import render,redirect
from .forms import AuthorForm, BookForm
from .models import Book

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        book_form = BookForm(request.POST)
        if author_form.is_valid():
            author = author_form.save()

        if book_form.is_valid():
            book = book_form.save()
        # redirect
        return redirect('index')


    all_books = Book.objects.all()

    author_form = AuthorForm()
    book_form = BookForm()
    return render(request, 'index.html', {'author_form': author_form, 'book_form': book_form,'all_books':all_books  })
