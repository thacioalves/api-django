from django.urls import path
from .views import ExercicioListCreate, ExercicioUpdateDelete

urlpatterns = [
    path('exercicios/', ExercicioListCreate.as_view(), name='exercicio-list'),
    path('exercicio/<int:pk>/', ExercicioUpdateDelete.as_view(), name='exercicio-detail'),
]