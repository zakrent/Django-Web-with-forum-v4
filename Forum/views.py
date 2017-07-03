from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from .forms import *
from django.core.paginator import Paginator
# Create your views here.


def index(request, page_number=1):
    if request.method == 'POST':
        form = Topic_Creation_Form(request.POST)
        if request.user.is_authenticated and form.is_valid():
            topic = Topic(name=form.cleaned_data['name'], creator=request.user)
            post = Post(content=form.cleaned_data['content'], creator=request.user)
            topic.save()
            post.topic = topic
            post.save()
            return redirect('forum:topic', topic.pk, 1)
    form = Topic_Creation_Form()
    topics = Topic.objects.all().order_by('-pk')
    paginator = Paginator(topics, 20)
    if int(page_number) > paginator.num_pages:
        return redirect('forum:index', 1)
    page = paginator.page(page_number)
    return render(request, 'Forum/index.html',
                  {
                      'page': page,
                      'form': form,
                      'submit_value': 'Create topic',
                      'last_page': paginator.num_pages
                  })


def topic(request, pk, page_number):
    if request.method == 'POST':
        post_form = Post_Form(request.POST)
        if request.user.is_authenticated and post_form.is_valid():
            post = post_form.save(commit=False)
            post.creator = request.user
            post.topic = get_object_or_404(Topic, pk=pk)
            post.save()
            return redirect('forum:topic', pk=pk, page_number=page_number)
        return redirect('forum:log_in')
    else:
        topic = get_object_or_404(Topic, pk=pk)
        posts = topic.posts.all()
        post_form = Post_Form()
        paginator = Paginator(posts, 20)
        page = paginator.page(page_number)
        return render(request, 'Forum/topic.html',
                      {
                        'topic': topic,
                        'submit_value': 'Post',
                        'page': page,
                        'form': post_form,
                        'last_page': paginator.num_pages
                      })


def log_in(request):
    if request.method == 'POST':
        form = User_LogIn_Form(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('forum:index')
    else:
        form = User_LogIn_Form()
    return render(request, 'Forum/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = User_Register_Form(request.POST)
        if form.is_valid():
            user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
            user.save()
            return redirect('forum:log_in')
    form = User_Register_Form
    return render(request, 'Forum/register.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect('forum:index')
