from .views import get, create, delete, update
from django.urls import path

urlpatterns = [
    path('get/', get.get_todo_list),
    path('get/<int:id>/', get.get_todo),
    path('delete/<int:id>/', delete.delete_todo),
    path('update/<int:id>/', update.update_todo),
    path('create/', create.create_todo),
]