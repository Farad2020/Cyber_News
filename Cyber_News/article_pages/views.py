from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from users.models import User
import json

from .models import *
from .forms import *


# Create your views here.


def get_all_articles(request):
    articles = Article.objects.filter(is_active=True)  # .order_by('-date')
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
        elif 'deactivate' in request.POST:
            article.is_active = False
        elif 'activate' in request.POST:
            article.is_active = True
        elif 'post_comment' in request.POST:
            try:
                txt = request.POST.get("comments_text")
                if not auto_banner(request, txt):
                    comment = Comment(comments_text=txt,
                                      article=Article.objects.get(pk=article_id),
                                      author=request.user, )
                    comment.save()
            except:
                print('the comments cannot be added')
        elif 'upvote_comment' in request.POST:
            like_comment = Comment.objects.get(id=request.POST.get('upvote_comment'))
            like_comment.upvoters.add(request.user)
            like_comment.save()
        elif 'remove_upvote_comment' in request.POST:
            remove_upv_comment = Comment.objects.get(id=request.POST.get('remove_upvote_comment'))
            remove_upv_comment.upvoters.remove(request.user)
            remove_upv_comment.save()
        elif 'reply_comment' in request.POST:
            comment = Comment.objects.get(id=request.POST.get('reply_comment'))
            my_str = str(comment.id)
            txt = request.POST.get("reply_text_" + my_str)
            if not auto_banner(request, txt):
                comment = Comment(comments_text=txt,
                                  article=Article.objects.get(pk=article_id),
                                  author=request.user, receiver=comment.author)
                comment.save()

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
    blogs = Blogs.objects.filter(is_active=True)  # .order_by('-date')
    return render(request, "article_pages/blogs_page.html", {'blogs': blogs})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)
    blog.numberOfClicks += 1
    blog.save()
    comments = showComments(request, None, blog_id)
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
        elif 'post_comment' in request.POST:
            try:
                txt = request.POST.get("comments_text")
                if not auto_banner(request, txt):
                    comment = Comment(comments_text=txt,
                                      blog=Blogs.objects.get(pk=blog_id),
                                      author=request.user, )
                    comment.save()
            except:
                print('the comments cannot be added')
        elif 'upvote_comment' in request.POST:
            like_comment = Comment.objects.get(id=request.POST.get('upvote_comment'))
            like_comment.upvoters.add(request.user)
            like_comment.save()
        elif 'remove_upvote_comment' in request.POST:
            remove_upv_comment = Comment.objects.get(id=request.POST.get('remove_upvote_comment'))
            remove_upv_comment.upvoters.remove(request.user)
            remove_upv_comment.save()
        elif 'reply_comment' in request.POST:
            comment = Comment.objects.get(id=request.POST.get('reply_comment'))
            my_str = str(comment.id)
            txt = request.POST.get("reply_text_" + my_str)
            if not auto_banner(request, txt):
                comment = Comment(comments_text=txt,
                                  blog=Blogs.objects.get(pk=blog_id),
                                  author=request.user, receiver=comment.author)
                comment.save()
    blog.save()
    return render(request, 'article_pages/blog_details_page.html', {'blog': blog,
                                                                    'comments': comments,
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
    threads = Thread.objects.all()  # .order_by('-date')
    return render(request, "article_pages/threads_page.html", {'threads': threads})


def thread_detail(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    comments = showComments(request, None, None, thread_id)
    if request.method == 'POST':
        if 'deactivate' in request.POST:
            print("False")
            thread.is_active = False
        if 'activate' in request.POST:
            print("True")
            thread.is_active = True
        elif 'post_comment' in request.POST:
            try:
                txt = request.POST.get("comments_text")
                if not auto_banner(request, txt):
                    comment = Comment(comments_text=txt,
                                      thread=Thread.objects.get(pk=thread_id),
                                      author=request.user, )
                    comment.save()
            except:
                print('the comments cannot be added')
        elif 'upvote_comment' in request.POST:
            like_comment = Comment.objects.get(id=request.POST.get('upvote_comment'))
            like_comment.upvoters.add(request.user)
            like_comment.save()
        elif 'remove_upvote_comment' in request.POST:
            remove_upv_comment = Comment.objects.get(id=request.POST.get('remove_upvote_comment'))
            remove_upv_comment.upvoters.remove(request.user)
            remove_upv_comment.save()
    thread.save()
    return render(request, 'article_pages/thread_details_page.html', {'thread': thread,
                                                                      'comments': comments,
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


def showComments(request, article_id=None, blog_id=None, thread_id=None, ):
    if article_id is not None:
        try:
            comments = Comment.objects.filter(article=Article.objects.get(pk=article_id)).order_by('-comment_date')
            return comments
        except:
            return "No comments yet"
    if blog_id is not None:
        try:
            comments = Comment.objects.filter(blog=Blogs.objects.get(pk=blog_id)).order_by('-comment_date')
            return comments
        except:
            return "No comments yet"
    if thread_id is not None:
        try:
            comments = Comment.objects.filter(thread=Thread.objects.get(pk=thread_id)).order_by('-comment_date')
            return comments
        except:
            return "No comments yet"


def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    form = EditCommentForm(request.POST or None, instance=comment)
    if form.is_valid():
        form.save()
        if comment.article is not None:
            return redirect('article_pages:article_det', comment.article.id)

        if comment.blog is not None:
            return redirect('article_pages:blog_det', comment.blog.id)

        if comment.thread is not None:
            return redirect('article_pages:thread_det', comment.thread.id)
    return render(request, "article_pages/edit_comment.html", {'form': form})


def auto_banner(request, txt):
    ban_user = False
    print("worked1")
    if request.user.is_moderator or request.user.is_superuser:
        return ban_user
    txt = str(txt)
    with open("static/bad_words.json", 'r') as my_json:
        vocabulary = json.load(my_json)
    print("worked3")

    for word in vocabulary:
        if txt.__contains__(word):
            ban_user = True
            break
    if ban_user:
        request.user.is_active = False
        print("worked3")
        request.user.save()
        return ban_user
    else:
        return ban_user
