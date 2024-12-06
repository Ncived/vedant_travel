# trips/views.py
from django.shortcuts import render, redirect
from .models import Destination

# Example view for the homepage (root path)
def home(request):
    return render(request, 'home.html')  # Render the home.html template

# View for the destination list
def destination_list(request):
    destinations = Destination.objects.all()  # Get all destinations from the database
    return render(request, 'trips/destination_list.html', {'destinations': destinations})

# View for the destination detail page
def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)  # Get the destination by its ID
    return render(request, 'trips/destination_detail.html', {'destination': destination})
