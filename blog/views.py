from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
from blog.models import Blog, Post, Poll, Choice
import blog.forms
from django import http


# Create your views here.
def blog_index (request, blog_slug):
    blog = get_object_or_404(Blog, slug=blog_slug)
    posts = Post.objects.filter(blog=blog)
    context = {
    'blog': blog,
    'posts': posts,
    }
    return TemplateResponse(request, 'blog.html', context)

def blog_post (request, blog_slug, post_slug):
    context = {
    'post': get_object_or_404(Post, slug=post_slug, blog__slug=blog_slug),
    }
    return TemplateResponse(request, 'blog_post.html', context)

def poll_index (request, poll_slug):
    choice  = blog.forms.ClassForm(request.POST or None)

    if request.method == 'POST':
        answer = request.POST.get('answer', '')
        check = get_object_or_404(Choice, id=answer, poll__slug=poll_slug)
        check.count()
        return http.HttpResponseRedirect('./results/')

    poll = get_object_or_404(Poll, slug=poll_slug)
    choices = Choice.objects.filter(poll=poll)

    context = {
    'poll': poll,
    'choices': choices,
    }
    return TemplateResponse(request, 'poll.html', context)

def results (request, poll_slug):
    poll = get_object_or_404(Poll, slug=poll_slug)

    context = {
    'poll': poll,
    }
    return TemplateResponse(request, 'results.html', context)
