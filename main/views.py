from  django.http import JsonResponse
from  .models import Diabetes
from .serializers import DiabetesSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
import joblib
import pandas as pd

@api_view(['POST'])
def analysis_diabetes(request):
    if request.method == 'POST':
        
        serializer = DiabetesSerializer(data=request.data)
        if serializer.is_valid():
            df = pd.DataFrame({
                'Pregnancies': [serializer.validated_data['Pregnancies']],
                'Glucose': [serializer.validated_data['Glucose']],
                'BloodPressure': [serializer.validated_data['BloodPressure']],
                'SkinThickness': [serializer.validated_data['SkinThickness']],
                'Insulin': [serializer.validated_data['Insulin']],
                'BMI': [CalculateBMI(serializer.validated_data['Weight'], (serializer.validated_data['Height'] / 100))],
                'DiabetesPedigreeFunction': [serializer.validated_data['DiabetesPedigreeFunction']],
                'Age': [serializer.validated_data['Age']]
            })
            model = joblib.load('diabetics-prediction-rfr.joblib')
            
            try:
                result = model.predict(df)
                serializer.validated_data['Percentage'] = result[0] * 100
                serializer.save()
                return JsonResponse({"Data": serializer.data}, status=status.HTTP_201_CREATED)
            
            except Exception as e:
                return JsonResponse({"error": f"Prediction error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def CalculateBMI(weight, height):
    return weight/(height*height)