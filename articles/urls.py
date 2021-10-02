from django.urls import path
from .views import (ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView)


urlpatterns = [
    path('', ArticleListView.as_view(), name='home'),
    path('posts/<int:pk>/', ArticleDetailView.as_view(), name="post_detail"),
    path('posts/new/', ArticleCreateView.as_view(), name="post_new"),
    path('posts/<int:pk>/edit/', ArticleUpdateView.as_view(), name="post_edit"),
    path('posts/<int:pk>/delete/', ArticleDeleteView.as_view(), name="post_delete")
]