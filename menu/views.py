from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import MenuItem


# Create your views here.
def menu(request):
    menu = MenuItem.objects.all().order_by('name')

    return render(
    request,
    'menu/menu.html',
    {
        'menu': menu
    }
  )
