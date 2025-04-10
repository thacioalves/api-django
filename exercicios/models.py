from django.db import models

class Exercicio(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    categoria = models.CharField(max_length=100)
    imagem_url = models.URLField()

    def str(self):
        return self.nome
