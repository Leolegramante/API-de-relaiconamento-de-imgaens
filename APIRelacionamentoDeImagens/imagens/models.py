from django.db import models


class Imagem(models.Model):
   foto = models.ImageField()
   descricao = models.CharField(max_length=50)
   data = models.DateTimeField(auto_now_add=True)

   def __str__(self):
       return self.descricao


class Pessoa(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class PessoaImagem(models.Model):
    foto = models.ForeignKey(Imagem, on_delete=models.CASCADE)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
