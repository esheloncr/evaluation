from django.contrib import admin
from .models import Employee, Evaluation


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name"
    ]


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = [
        "evaluation_body",
        "rating"
    ]
