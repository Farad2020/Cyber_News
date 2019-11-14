from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from .forms import *
# Create your views here.


def profile(request):
    return render(request, "User_Account/user_page.html")


class registerView(CreateView):
    form_class = SimpleUserForm
    success_url = reverse_lazy('login')
    template_name = 'User_Account/register.html'