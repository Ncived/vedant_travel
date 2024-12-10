from django.shortcuts import render, get_object_or_404
from .models import Destination

# Home page view (root path)
def home(request):
    return render(request, 'index.html')  # Ensure index.html is in your templates folder

# View for the destination list
def destination_list(request):
    destinations = Destination.objects.all()  # Get all destinations from the database
    return render(request, 'trips/destination_list.html', {'destinations': destinations})

# View for the destination detail page
def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)  # Get the destination by its ID
    return render(request, 'trips/destination_detail.html', {'destination': destination})
