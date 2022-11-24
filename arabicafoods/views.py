from django.shortcuts import render
from .models import Item

# Create your views here.
def get_home(request):
    return render(request, '../templates/home/home.html')

def make_reservation(request):
    items = Item.objects.all
    context = {
        'items' : items
    }
    return render(request, '../templates/home/reservation.html', context)

def go_to_menu(request):
    return render(request, '../templates/home/menu.html')

def go_to_contact(request):
    return render(request, '../templates/home/contact.html')    