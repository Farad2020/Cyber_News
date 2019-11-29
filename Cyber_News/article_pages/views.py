from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from users.models import User
from .models import *
from .forms import  *
# Create your views here.


def get_all_articles(request):
    articles = Article.objects.all
    return render(request,"article_pages/articles_page.html", {'articles':articles})


def create_article_page(request):
    form = EditArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = EditArticleForm()

    return render(request, "Cyber_News_App/article_creation_page.html", {'form': form})


def article_details(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.numberOfClicks += 1
    article.save()
    comments = showComments(request, article_id)

    if request.method == 'POST':
        try:
            txt = request.POST.get("comments_text")
            # print(request.POST)
            comment = Comments(comments_text=txt,
                               article=Article.objects.get(pk=article_id),
                               author= request.user)
            comment.save()
        except:
            print('the comments cannot be added')

    #author = User.objects.get(pk=article.author_id_id)  # why id_id works!&? 'author': author 'comment' : comments,
    return render(request, 'article_pages/article_details_page.html', {'article': article,
                                                                       'comments':comments,})
                       
def articles_delete(request, id=None):

    article= get_object_or_404(Article, id=id)

    creator= article.user.username

    if request.method == "POST" and request.user.is_authenticated and request.user.username == creator:
        article.delete()
        messages.success(request, "Post successfully deleted!")
        return HttpResponseRedirect("/article_pages/article_details_page.html/")
    
    context= {'article': article,
              'creator': creator,
              }
    
    return render(request, 'article_pages/articles_delete.html', context)

def edit_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    form = EditArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        form = EditArticleForm()
        return redirect('../')
    return render(request, "article_pages/edit_article.html", {'form': form})

def addComment(request, article_id):
    try:
        txt = request.POST.get("comments_text")
        comment = Comments(comments_text=txt,
                            article=Article.objects.get(pk=article_id),
                            )
        comment.save()
        return render(request, "article_pages/article_details_page.html",
                                {"article":Article.objects.get(pk=article_id)})
    except:
        return HttpResponse("No such articles")

def showComments(request, article_id):
    try:
        comments = Comments.objects.filter(article=Article.objects.get(pk=article_id))
        return comments
    except:
        return "No comments yet"
                                                                  

