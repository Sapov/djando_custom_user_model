from django.urls import path

from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='ArticleList'),
    path('<int:pk>/edit', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/edit', views.ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/edit', views.ArticleDeleteView.as_view(), name='article_delete'),


]
