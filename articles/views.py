from django.views.generic import ListView, DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)



from .models import Post


class ArticleListView(ListView):
    model = Post
    template_name = "home.html"


class ArticleDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class ArticleCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body", "date"]


class ArticleUpdateView(UpdateView):
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]

    def test_func(self):
        obj = self.get_object()   
        return obj.author == self.request.user

class ArticleDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        obj = self.get_object()   
        return obj.author == self.request.user