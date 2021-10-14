from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.views.generic import ListView

from advito.models import Post, Category
from advito.forms import PostForm

# Create your views here.

class IndexView(ListView):
    model = Post
    template_name = 'advito/index.html'
    context_object_name = 'posts'
    extra_context = {'page_title': '7 last posts'}

    def get_queryset(self):
        return self.model.objects.all()[:7]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context

# def index(request):
#     posts = Post.objects.all()[:7]
#     return render(request, 'advito/index.html', {'posts': posts, 'page_title': '7 last posts'})

    # return HttpResponse(f'id:{post.id}|title:{post.title}\n' for post in posts)

class AnnouncementView(ListView):
    model = Post
    template_name = 'advito/announcement.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(AnnouncementView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context


# def announcement(request):
#     posts = Post.objects.all()
#     return render(request, 'advito/announcement.html', {'posts': posts, 'page_title': 'All posts'})
#     # return HttpResponse('announcement')

def post_detail(request, post_id):
    # try:
    #     post = Post.objects.get(id=post_id)
    # except: Post.DoesNotExist:
    #     raise Http404('page not exist')
    post = get_object_or_404(Post, id=post_id)

    return render(request, 'advito/detail.html', {'post': post, 'page_title': 'Post detail'})

def post_create(request):
    form = PostForm()

    if request.method == 'GET':
        return render(request, 'advito/post_create.html', {'form': form, 'page_title': 'Post create'})
    elif request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(reverse('advito:post_detail', kwargs={'post_id': post.id}))
        else:
            return render(request, 'advito/post_create.html', {'form': form, 'page_title': 'Post create'})

def post_edit(request, post_id):
    return HttpResponse('Post edit')

def post_delete(request, post_id):
    return HttpResponse('Post delete')

def category(request):
    categorys = Category.objects.all()
    return render(request, 'advito/category.html', {'categorys': categorys, 'page_title': 'All category'})

def choise_category(request, category_id):
    posts = Post.objects.filter(category=category_id)
    category = Category.objects.get(id=category_id)
    return render(request, 'advito/category_detail.html', {'posts': posts, 'category': category})



