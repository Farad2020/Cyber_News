from django.shortcuts import render

# Create your views here.
def get_all_games(request):
    #games = Game.objects.all().order_by('game_name'){'games': games}
    return render(request, "game_pages/games_page.html")


"""
def games_page(request):
    games = Game.objects.all().order_by('game_name')
    return render(request, "Cyber_News_App/games_page.html", {'games': games})


def create_game_page(request):
    if request.method == 'POST':
        try:
            game = Game(game_name=request.POST.get("game_name"), game_developer=request.POST.get("game_dev"),
                        game_publisher=request.POST.get("game_pub"), game_text=request.POST.get("game_desc"),
                        game_rd=request.POST.get("game_date"), game_rating=request.POST.get("game_rate"))
            game.save()
        except:
            print('the comments cannot be added')
    return render(request, "Cyber_News_App/game_creation_page.html", {})


def game_details(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, "Cyber_News_App/game_details_page.html", {'game': game})
"""
