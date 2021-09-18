from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")

    def __str__(self):
        return self.first_name


class Evaluation(models.Model):
    evaluation_body = models.TextField(verbose_name="Отзыв")
    rating = models.PositiveIntegerField(verbose_name="Оценка")

    def __str__(self):
        return 'Отзыв'
