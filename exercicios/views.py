from rest_framework import generics
from .models import Exercicio
from .serializers import ExercicioSerializer

class ExercicioListCreate(generics.ListCreateAPIView):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer

class ExercicioUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercicio.objects.all()
    serializer_class = ExercicioSerializer