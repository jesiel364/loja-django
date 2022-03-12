from django.db import models
from djmoney.models.fields import MoneyField

class Base(models.Model):
  criacao = models.DateTimeField(auto_now_add=True)
  atualizacao = models.DateTimeField(auto_now=True)
  ativo = models.BooleanField(default=True)
  
  class Meta:
    abstract = True
    
class Produto(Base):
  titulo = models.CharField(max_length=255)
  marca = models.CharField(max_length=255)
  preco = MoneyField(max_digits=14, decimal_places=2, default_currency='BRL')
  #models.DecimalField(max_digits=5000, decimal_places=2)
  
  class Meta:
    verbose_name = 'Produto'
    verbose_name_plural = 'Produtos'
    
  def __str__(self):
    return self.titulo

class Estoque(Base):
  produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
  codigo = models.CharField(max_length=8, default='123456am')
  quantidade = models.IntegerField()
  locacao = models.CharField(max_length=255, default='1A01', verbose_name='locação')
  excesso = models.CharField(max_length=255, blank=True, default='')
  
  class Meta:
    verbose_name = 'Estoque'
    verbose_name_plural= 'Estoques'
    
  def __str__(self):
    return f'{self.produto} esta com {self.quantidade} unidades nas locações {self.locacao} e excesso {self.excesso}'