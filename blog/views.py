from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'blog/post_list.html', {'posts' : posts})
	
@login_required
def post_unpublished(request):
	posts = Post.objects.filter(published_date__isnull=True).order_by('created_date');
	return render(request, 'blog/post_list.html', {'posts' : posts})
	
@login_required
def post_publish(request, post_id):
	posts = get_object_or_404(Post, pk=post_id)
	posts.publish();
	return redirect('blog.views.post_detail', post_id=posts.pk)

def post_detail(request, post_id):
	posts = get_object_or_404(Post, pk=post_id)
	return render(request, 'blog/post_detail.html', {'post' : posts})
	
@login_required
def post_delete(request, post_id):
	posts = get_object_or_404(Post, pk=post_id)
	posts.delete()
	return redirect('blog.views.post_list')

@login_required
def post_new(request):
	"""This method will make new posts that are not published yet"""
	if(request.method == "POST"):
		form = PostForm(request.POST)
		if(form.is_valid()):
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('blog.views.post_detail', post_id=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form' : form})
	
@login_required
def post_edit(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	if(request.method == "POST"):
		form = PostForm(request.POST, instance=post)
		if(form.is_valid()):
			post = form.save(commit=False)
			post.author = request.user
			post.save()
			return redirect('blog.views.post_detail', post_id=post.pk)
	else:
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form' : form})	