from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from evaluation.models import Employee, Evaluation
from .serializers import EmployeeSerializer, EvaluationSerializer


class EmployeeAPIView(APIView):
    def get(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return JsonResponse({"Employees": serializer.data}, safe=False)


class EvaluationAPIView(APIView):
    def get(self, request):
        queryset = Evaluation.objects.all()
        serializer = EvaluationSerializer(queryset, many=True)
        return JsonResponse({"Reviews": serializer.data}, safe=False)

    def post(self, request):
        data = request.data
        serializer = EvaluationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return JsonResponse({"message": "created"}, status=status.HTTP_201_CREATED)
