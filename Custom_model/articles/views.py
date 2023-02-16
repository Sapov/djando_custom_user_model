from django.shortcuts import render
from . import models
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView, DeleteView


# Create your views here.
class ArticleListView(ListView):
    model = models.Articles
    template_name = 'article_list.html'

class ArticleUpdateView(UpdateView):
    model = models.Articles
    template_name = 'article_edit.html'

class ArticleDetailView(DetailView):
    model = models.Articles
    template_name = 'article_detail.html'

class ArticleDeleteView(DeleteView):
    model = models.Articles
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
