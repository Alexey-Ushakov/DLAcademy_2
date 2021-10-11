from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from advito.models import Post, Category
# Create your views here.

def index(request):
    posts = Post.objects.all()[:7]
    return render(request, 'advito/index.html', {'posts': posts, 'page_title': '7 last posts'})

    # return HttpResponse(f'id:{post.id}|title:{post.title}\n' for post in posts)

def announcement(request):
    posts = Post.objects.all()
    return render(request, 'advito/announcement.html', {'posts': posts, 'page_title': 'All posts'})
    # return HttpResponse('announcement')

def post_detail(request, post_id):
    # try:
    #     post = Post.objects.get(id=post_id)
    # except: Post.DoesNotExist:
    #     raise Http404('page not exist')
    post = get_object_or_404(Post, id=post_id)

    return render(request, 'advito/detail.html', {'post': post, 'page_title': 'Post detail'})

def post_create(request):
    return HttpResponse('Post create')

def post_edit(request, post_id):
    return HttpResponse('Post edit')

def post_delete(request, post_id):
    return HttpResponse('Post delete')

def category(request):
    categorys = Category.objects.all()
    return render(request, 'advito/category.html', {'categorys': categorys, 'page_title': 'All category'})

def choise_category(request, category_id):
    posts = Post.objects.filter(category=category_id)
    category = Category.objects.get(category=category_id)
    return render(request, 'advito/category_detail.html', {'posts': posts, 'page_title': category.title})



