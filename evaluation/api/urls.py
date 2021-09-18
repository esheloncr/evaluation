from django.urls import path
from .views import EmployeeAPIView, EvaluationAPIView

urlpatterns = [
    path("employees", EmployeeAPIView.as_view()),
    path("reviews", EvaluationAPIView.as_view())
]