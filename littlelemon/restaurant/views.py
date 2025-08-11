from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import MenuSerializer, BookingSerializer
from .models import Booking
from .models import Menu

# Create your views here.
# Define index view
def index(request):
    return render(request, 'index.html', {})

# Define views for Menu items
class MenuItemsView(generics.ListCreateAPIView): 
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):     
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Define views for Booking items
class BookingViewSet(viewsets.ModelViewSet):
    # Ensure only authenticated users can access booking views
    permission_classes = [IsAuthenticated] 

    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    