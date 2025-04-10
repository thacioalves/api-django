from django.db import models

class Exercicio(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()

    def str(self):
        return self.nome
