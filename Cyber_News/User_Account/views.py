from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
# Create your views here.

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
    return render(request, 'User_Account/signup_page.html', {'form': form})