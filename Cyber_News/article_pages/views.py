from django.shortcuts import render

# Create your views here.
def det_all_articles(request):
    return render(request,"article_pages/articles_page.html")


"""
def games_page(request):
    games = Article.objects.all().order_by('article_name')
    return render(request, "Cyber_News_App/articles_page.html", {'articles': articles})


def create_article_page(request):
    if request.method == 'POST':
        try:
            article = Article(article_name=request.POST.get("article_name"), article_text=request.POST.get("article_text"),
                        article_date=request.POST.get("article_data"), author_id=request.POST.get("author_id"),
                        game_id=request.POST.get("game_id"), rating=request.POST.get("article_rate"),
                        numberOfClicks=request.POST.get("numberOfClicks"),isBlog=request.POST.get("isBlog"))
            article.save()
        except:
            print('the comments cannot be added')
    return render(request, "Cyber_News_App/article_creation_page.html", {})


def article_details(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.numberOfClicks += 1
    article.save()

    author = User.objects.get(pk=article.author_id_id)  # why id_id works!&?
    return render(request, 'Cyber_News_App/article_detail.html', {'article': article,
                                                                  'author': author})
"""
