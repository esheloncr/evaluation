Задача: Приложение "Оценка"

Представим, что какая-то организация решила создать приложение для оценки своих сотрудников.
Ваша задача создать бэк-энд для этого приложения.
Они хотят создать приложение, которое будет общаться с вашим проектом через REST-API.
От вас требуется: 3 REST запроса, одни для получения списка сотрудников, второй для получения всех отзывов, а третий для того, чтобы оставить отзыв на сотрудника. Панель администратора, в которой можно увидеть/добавить/удалить сотрудников и отзывы.

Необходимо создать Django проект.
Архитектура проекта должна быть следующей: 

Название проекта
--Название приложения
----api
-----serializers.py
-----urls.py
-----views.py
----admin.py
----urls.py
----wsgi.py
--manage.py
--requirements.txt

venv не обязательно, но будет плюсом