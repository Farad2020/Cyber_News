from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .models import *


def homepage(request):
    # return HttpResponse("homepage")
    return render(request, 'Cyber_News_App/homepage_test.html')


def index(request):
    articles = Article.objects.all().order_by('article_date')
    return render(request, 'Cyber_News_App/articles.html', {'articles': articles})


def article_details(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.numberOfClicks += 1
    article.save()

    author = Editor.objects.get(pk=article.author_id_id)  # why id_id works!&?
    return render(request, 'Cyber_News_App/article_detail.html', {'article': article,
                                                                  'author': author})


def contacts(request):
    return render(request, 'Cyber_News_App/contacts.html')


"""
def sign_up(request):
    # return HttpResponse("user login page")
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            redirect('cyber_news:index')
    else:
        form = UserCreationForm()
    return render(request, 'Cyber_News_App/signup_page.html', {'form': form})
"""

'''def user_page(request, user_id):
    user = get_object_or_404(SimpleUser, pk = user_id)
    user.save()
    return render(request, 'Cyber_News_App/login.html', {'user':user})'''

