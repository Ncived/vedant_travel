from django.shortcuts import render, get_object_or_404, redirect
from .models import Destination, Booking
from .forms import DestinationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# pylint: disable=too-many-ancestors, missing-class-docstring, too-few-public-methods,disable=no-member, trailing-whitespace

# Module-level docstring
"""
Views for handling trip-related operations, including managing destinations, bookings, and user signups.
"""

def home(request):
    """Render the home page."""
    return render(request, 'trips/home.html')

def about(request):
    """Render the about page."""
    return render(request, 'trips/about.html')

def destination_list(request):
    """List all destinations."""
    destinations = Destination.objects.all()
    return render(request, 'trips/destination_list.html', {'destinations': destinations})

def destination_detail(request, pk):
    """Show details for a specific destination."""
    destination = get_object_or_404(Destination, pk=pk)
    return render(request, 'trips/destination_detail.html', {'destination': destination})

def booking_create(request, destination_pk):
    """Create a new booking for a destination."""
    destination = get_object_or_404(Destination, pk=destination_pk)
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        travelers = int(request.POST.get('travelers'))
        if travelers <= destination.availability:
            Booking.objects.create(user_name=user_name, destination=destination, travelers=travelers)
            destination.availability -= travelers
            destination.save()
            return redirect('destination_list')
        else:
            return render(request, 'trips/booking_form.html', {'destination': destination, 'error': "Not enough availability!"})
    return render(request, 'trips/booking_form.html', {'destination': destination})

@login_required
def destination_create(request):
    """Create a new destination (only for logged-in users)."""
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('destination_list')
    else:
        form = DestinationForm()
    return render(request, 'trips/destination_form.html', {'form': form})

@login_required
def destination_update(request, pk):
    """Update an existing destination (only for logged-in users)."""
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        form = DestinationForm(request.POST, instance=destination)
        if form.is_valid():
            form.save()
            return redirect('destination_list')
    else:
        form = DestinationForm(instance=destination)
    return render(request, 'trips/destination_form.html', {'form': form})

@login_required
def destination_delete(request, pk):
    """Delete an existing destination (only for logged-in users)."""
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        destination.delete()
        return redirect('destination_list')
    return render(request, 'trips/destination_confirm_delete.html', {'destination': destination})

def signup(request):
    """Handle user signup."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful signup
            return redirect('destination_list')  # Redirect to destination list after signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def explore(request):
    """Render a page with a list of example destinations and itineraries."""
    destinations = [
        {
            'name': 'Paris',
            'image_url': 'https://th.bing.com/th/id/OIP.gOiajMIog2Kbarg3VMx9RwHaE8?rs=1&pid=ImgDetMain',
            'description': 'Paris, the capital city of France, is known for its art, fashion, and culture.',
            'itinerary': [
                'Day 1: Visit the Eiffel Tower',
                'Day 2: Explore the Louvre Museum',
                'Day 3: Day trip to Versailles',
                'Day 4: Take a Seine river cruise',
                'Day 5: Walk around Montmartre and visit the Sacré-Cœur'
            ],
            'best_time_to_visit': 'April to June and September to October'
        },
        {
            'name': 'New York City',
            'image_url': 'https://th.bing.com/th/id/OIP.-TzFBbHeO7cr_QR7Z466wQHaE8?rs=1&pid=ImgDetMain',
            'description': 'New York City is known for its iconic landmarks, Broadway shows, and diverse neighborhoods.',
            'itinerary': [
                'Day 1: Visit the Statue of Liberty',
                'Day 2: Explore Central Park and the Met',
                'Day 3: Walk across the Brooklyn Bridge',
                'Day 4: Visit the 9/11 Memorial and Museum',
                'Day 5: See a Broadway Show'
            ],
            'best_time_to_visit': 'April to June and September to early November'
        },
        {
            'name': 'Rome',
            'image_url': 'https://th.bing.com/th/id/OIP.INB7nsN_TGttYNu4sINevQHaEW?rs=1&pid=ImgDetMain',
            'description': 'Rome, the capital of Italy, is known for its ancient monuments, art, and architecture.',
            'itinerary': [
                'Day 1: Visit the Colosseum and Roman Forum',
                'Day 2: Explore the Vatican Museums and St. Peter\'s Basilica',
                'Day 3: Walk around the Spanish Steps and Trevi Fountain',
                'Day 4: Visit the Pantheon and Piazza Navona',
                'Day 5: Day trip to Pompeii'
            ],
            'best_time_to_visit': 'April to June and September to October'
        },
        {
            'name': 'Sydney',
            'image_url': 'https://th.bing.com/th/id/OIP.8AZsvjI3-khUnhL08bI_yAHaE8?rs=1&pid=ImgDetMain',
            'description': 'Sydney, Australia’s largest city, is famous for its Opera House and beautiful harbor.',
            'itinerary': [
                'Day 1: Visit the Sydney Opera House',
                'Day 2: Explore Bondi Beach',
                'Day 3: Walk across the Sydney Harbour Bridge',
                'Day 4: Visit Taronga Zoo',
                'Day 5: Day trip to the Blue Mountains'
            ],
            'best_time_to_visit': 'September to November and March to May'
        }
    ]

    return render(request, 'trips/explore.html', {'destinations': destinations})
