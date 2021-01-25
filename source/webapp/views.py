from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from django.urls import reverse
from webapp.forms import BookAddForm
from webapp.models import Book


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'books'
    model = Book


class BookAddView(CreateView):
    template_name = 'create.html'
    model = Book
    form_class = BookAddForm
    success_url = reverse_lazy('webapp:index')

    def form_valid(self, form):
        form.instance.author_name = self.request.user
        return super().form_valid(form)


class BookDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Book
    context_object_name = 'book'
    success_url = reverse_lazy('webapp:index')


class BookView(DetailView):
    template_name = 'detail.html'
    context_object_name = 'book'
    model = Book
    success_url = reverse_lazy('webapp:index')


def add_book_to_friends(request, id):
    if request.is_ajax():
        book = get_object_or_404(Book, id=id)
        request.book.is_favorites.add(book)
        request.user.profile.save()
        return HttpResponse("hello world")
    else:
        return redirect(reverse('webapp:index'))


def remove_book_from_friends(request, id):
    if request.is_ajax():
        book = get_object_or_404(Book, id=id)
        request.book.is_favorites.remove(book)
        request.user.profile.save()
        return HttpResponse("hello world")
    else:
        return redirect(reverse('webapp:index'))
