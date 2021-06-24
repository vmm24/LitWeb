from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):

    return render(request,'blog/home.html')

def about(request):
    context = {
    'posts':Post.objects.filter(status=1).order_by('-date')
    }
    return render(request,'blog/about.html',context)

class PostListView(ListView):
    queryset = Post.objects.filter(status=1).order_by('-date')
    template_name='blog/about.html'

class PostDetailView(DetailView):
    model=Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model=Post
    fields = ['title', 'content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Post
    fields = ['title', 'content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Post
    success_url = '/about'

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False
