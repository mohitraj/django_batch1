from django.shortcuts import render, redirect, get_object_or_404
from .form import PostForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post
from django.views.generic  import CreateView,DetailView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User


def home(request): # this is the object of HttpResponse
	
	return render(request, 'blog1/home.html', {'title': 'Batch1'})

def AllPost(request):
	posts = Post.objects.all()
	context = {'posts': posts}
	return render(request,'blog1/all_posts.html',context)

@login_required(login_url='login')
def CreatePost(request):
	form = PostForm()
	context = {'form':form, 'legend':"Post Now"}

	if request.method=='POST':
		form = PostForm(request.POST)
		if form.is_valid():
			mark1=form.save(commit=False)
			mark1.author =request.user
			form.save()
			return redirect("blog_allpost")
	return render(request,'blog1/form_display.html', context)


class PostCreateView(LoginRequiredMixin,CreateView):
	model = Post
	login_url = '/login/'
	fields = ['title','content']
	template_name = 'blog1/form_display.html'

	def form_valid(self,form):
		form.instance.author= self.request.user 
		return super().form_valid(form)

class PostDetailsView(LoginRequiredMixin,DetailView):
	model = Post

class PostListView(LoginRequiredMixin,ListView):
	model = Post 
	login_url = '/login_url/'
	context_object_name = 'posts'
	template_name = 'blog1/all_post_cls.html'
	ordering = ['-date1']
	paginate_by = 2



class UserPostListView(LoginRequiredMixin,ListView):
	model = Post 
	login_url = '/login_url/'
	context_object_name = 'posts'
	template_name = 'blog1/all_post_cls.html'
	ordering = ['-date1']
	paginate_by = 2

	#def get_queryset(self):
	#	print ("username s ", self.request.user)
	#	return Post.objects.all(author=)

	def get_queryset(self):

		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	login_url = '/login/'
	fields = ['title','content']
	template_name = 'blog1/form_display.html'

	def form_valid(self,form):
		form.instance.author= self.request.user 
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user ==post.author:
			return True 
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
	model = Post 
	success_url = '/blog/post/view/'

	def test_func(self):
		post = self.get_object()
		if self.request.user ==post.author:
			return True 
		return False