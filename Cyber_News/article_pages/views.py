from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from users.models import User
from .models import *
from .forms import *


# Create your views here.


def get_all_articles(request):
    articles = Article.objects.filter(is_active=True)        #.order_by('-date')
    return render(request, "article_pages/articles_page.html", {'articles': articles})


def create_article_page(request):
    form = EditArticleForm(request.POST or None, request.FILES)
    if form.is_valid():
        article = form.save(False)
        article.author_id = request.user
        article.save()
        return redirect('article_pages:article_pages')
    return render(request, "article_pages/article_creation_page.html", {'form': form})


def article_details(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.numberOfClicks += 1
    article.save()
    comments = showComments(request, article_id)

    if request.method == 'POST':
        if 'upvote' in request.POST:
            if request.user in article.article_score.all():
                article.article_score.remove(request.user)
            else:
                article.article_score.add(request.user)
        if 'deactivate' in request.POST:
                print("False")
                article.is_active = False
        if 'activate' in request.POST:
                print("True")
                article.is_active = True
        else:
            try:
                txt = request.POST.get("comments_text")
                # print(request.POST)
                comment = Comment(comments_text=txt,
                              article=Article.objects.get(pk=article_id),
                              author=request.user)
                comment.save()
            except:
                print('the comments cannot be added')

    article.save()
    # author = User.objects.get(pk=article.author_id_id)  # why id_id works!&? 'author': author 'comment' : comments,
    return render(request, 'article_pages/article_details_page.html', {'article': article,
                                                                       'comments': comments, })


def edit_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    form = EditArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('../')
    return render(request, "article_pages/edit_article.html", {'form': form})





def get_all_blogs(request):
    blogs = Blogs.objects.filter(is_active=True)     #.order_by('-date')
    return render(request, "article_pages/blogs_page.html", {'blogs': blogs})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    blog.numberOfClicks += 1
    blog.save()
    if request.method == 'POST':
        if 'upvote' in request.POST:
            if request.user in blog.blog_score.all():
                blog.blog_score.remove(request.user)
            else:
                blog.blog_score.add(request.user)
        if 'deactivate' in request.POST:
            print("False")
            blog.is_active = False
        if 'activate' in request.POST:
            print("True")
            blog.is_active = True
    blog.save()

    '''
    comments = showComments(request, blog_id)
    if request.method == 'POST':
        try:
            txt = request.POST.get("comments_text")
            # print(request.POST)
            comment = Comment(comments_text=txt,
                              article=Article.objects.get(pk=article_id),
                              author=request.user)
            comment.save()
        except:
            print('the comments cannot be added')
    '''
    return render(request, 'article_pages/blog_details_page.html', {'blog': blog,
                                                                       #'comments': comments,
                                                                       })


def create_blog(request):
    form = EditBlogForm(request.POST or None, request.FILES)
    if form.is_valid():
        blog = form.save(False)
        blog.author_id = request.user
        blog.save()
        return redirect('article_pages:blog_pages')
    return render(request, "article_pages/blog_creation_page.html", {'form': form})


def edit_blog(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    form = EditBlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('../')
    return render(request, "article_pages/edit_blog.html", {'form': form})





def get_all_threads(request):
    threads = Thread.objects.all()      #.order_by('-date')
    return render(request, "article_pages/threads_page.html", {'threads': threads})


def thread_detail(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    if request.method == 'POST':
        if 'deactivate' in request.POST:
            print("False")
            thread.is_active = False
        if 'activate' in request.POST:
            print("True")
            thread.is_active = True

    thread.save()
    '''
    comments = showComments(request, blog_id)
    if request.method == 'POST':
        try:
            txt = request.POST.get("comments_text")
            # print(request.POST)
            comment = Comment(comments_text=txt,
                              article=Article.objects.get(pk=article_id),
                              author=request.user)
            comment.save()
        except:
            print('the comments cannot be added')
    '''
    return render(request, 'article_pages/thread_details_page.html', {'thread': thread,
                                                                       #'comments': comments,
                                                                       })


def create_thread(request):
    form = EditThreadForm(request.POST or None, request.FILES)
    if form.is_valid():
        thread = form.save(False)
        thread.author_id = request.user
        thread.save()
        return redirect('article_pages:thread_pages')
    return render(request, "article_pages/thread_creation_page.html", {'form': form})


def edit_thread(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    form = EditBlogForm(request.POST or None, instance=thread)
    if form.is_valid():
        form.save()
        return redirect('../')
    return render(request, "article_pages/edit_thread.html", {'form': form})





def addComment(request, article_id):
    try:
        txt = request.POST.get("comments_text")
        comment = Comment(comments_text=txt,
                          article=Article.objects.get(pk=article_id),
                          )
        comment.save()
        return render(request, "article_pages/article_details_page.html",
                      {"article": Article.objects.get(pk=article_id)})
    except:
        return HttpResponse("No such articles")


def showComments(request, article_id):
    try:
        comments = Comment.objects.filter(article=Article.objects.get(pk=article_id))
        return comments
    except:
        return "No comments yet"
