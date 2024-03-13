from django.http import JsonResponse
from .models import MiningData

def get_mining_data(request):
    mining_data = MiningData.objects.all().values() 
    return JsonResponse(list(mining_data), safe=False)