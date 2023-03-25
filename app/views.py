from django.shortcuts import render
from .models import Drinks
from .serializers import DrinkSerializer
from django.http import JsonResponse

# Create your views here.

def drink_list(request):
    drinks  = Drinks.objects.all()
    # serialize the drinks 
    serializer = DrinkSerializer (drinks, many=True)
    return JsonResponse({'DRINKS':serializer.data}, safe=False)

