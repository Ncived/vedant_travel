from django.shortcuts import render, get_object_or_404, redirect
from .models import Destination, Booking
from django.http import HttpResponse
from .forms import DestinationForm  
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'trips/home.html')

def destination_list(request):
    destinations = Destination.objects.all()  # Get all destinations
    return render(request, 'trips/destination_list.html', {'destinations': destinations})

def destination_detail(request, pk):
    destination = get_object_or_404(Destination, pk=pk)  # Get the destination by primary key (pk)
    return render(request, 'trips/destination_detail.html', {'destination': destination})

def booking_create(request, destination_pk):
    destination = get_object_or_404(Destination, pk=destination_pk)  # Get the destination
    if request.method == 'POST':
        user_name = request.POST.get('user_name')  # Get the user name
        travelers = int(request.POST.get('travelers'))  # Get the number of travelers
        if travelers <= destination.availability:  # Check if availability allows for booking
            Booking.objects.create(user_name=user_name, destination=destination, travelers=travelers)
            destination.availability -= travelers  # Update availability
            destination.save()
            return redirect('destination_list')  # Redirect after successful booking
        else:
            return render(request, 'trips/booking_form.html', {'destination': destination, 'error': "Not enough availability!"})
    return render(request, 'trips/booking_form.html', {'destination': destination})  # GET request, show the form

# Create view for adding a new destination
def destination_create(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('destination_list')  # Redirect to the list of destinations
    else:
        form = DestinationForm()
    return render(request, 'trips/destination_form.html', {'form': form})

# Update view for editing an existing destination
def destination_update(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        form = DestinationForm(request.POST, instance=destination)
        if form.is_valid():
            form.save()
            return redirect('destination_list')
    else:
        form = DestinationForm(instance=destination)
    return render(request, 'trips/destination_form.html', {'form': form})

# Delete view for deleting an existing destination
def destination_delete(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    if request.method == 'POST':
        destination.delete()
        return redirect('destination_list')  # Redirect to destination list
    return render(request, 'trips/destination_confirm_delete.html', {'destination': destination})
    

# Signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful signup
            return redirect('home')  # Redirect to the home page after signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required  # Only logged-in users can access this view
def destination_create(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('destination_list')  # Redirect to the list of destinations
    else:
        form = DestinationForm()
    return render(request, 'trips/destination_form.html', {'form': form})
