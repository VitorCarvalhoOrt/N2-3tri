from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.

class Genero(models.Model):
    nome = models.CharField(max_length=128)

    def __str__(self):
        return self.nome

class Plataforma(models.Model):
    nome = models.CharField(max_length=128)

    def __str__(self):
        return self.nome

class Jogo(models.Model):
    nome = models.CharField(max_length=128)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    data_lancamento = models.DateField('LANÇAMENTO')
    descricao = models.TextField('Descrição', blank=True, default='')
    foto = models.ImageField(upload_to='capas/')

    destaque = models.BooleanField('DESTAQUE', default=False)

    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    plataformas = models.ManyToManyField(Plataforma)

    def __str__(self):
        return self.nome

class Review(models.Model):
    autor = models.CharField('Visitante', max_length=128)
    nota = models.IntegerField('Nota', validators=[MinValueValidator(1), MaxValueValidator(5)])
    comentario = models.TextField('Comentário')

    jogo = models.ForeignKey(Jogo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.autor} - {self.jogo.nome} ({self.nota} de 5)'
