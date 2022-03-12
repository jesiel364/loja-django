from django.contrib import admin
from .models import Produto, Estoque

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
  list_display = ('titulo', 'marca', 'preco', 'criacao', 'atualizacao', 'ativo')
  
@admin.register(Estoque)
class EstoqueAdmin(admin.ModelAdmin):
  list_display = ('codigo', 'produto', 'quantidade', 'locacao', 'excesso', 'criacao', 'ativo')