from django.shortcuts import render

# Create your views here.
def get_home(request):
    return render(request, '../templates/home/home.html')

def make_reservation(request):
    return render(request, '../templates/home/reservation.html')