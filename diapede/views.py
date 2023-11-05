from  django.http import JsonResponse
from  .models import Diabetes
from .serializers import DiabetesSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@api_view(['POST'])
def analysis_diabetes(request):
    if request.method == 'POST':
        serializer = DiabetesSerializer(data=request.data)
        # get all component
        # input into model
        # return the percentage


        if serializer.is_valid():
            serializer.validated_data['Percentage'] = 1.0
            serializer.save()
            return JsonResponse({"Data" : serializer.data},status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=400)