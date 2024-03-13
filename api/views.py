from django.http import JsonResponse
from .models import MiningData
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


def get_mining_data(request):
    mining_data = MiningData.objects.all().values() 
    return JsonResponse(list(mining_data), safe=False)


class MiningDataListView(APIView):
    def get(self, request):
        mining_data = MiningData.objects.all()
        serializer = MiningSerializer(mining_data, many=True)
        return Response(serializer.data)
