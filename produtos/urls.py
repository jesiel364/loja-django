from django.urls import path
from produtos.views import ProdutoListView, EstoqueListView, home_view
from produtos.models import Produto

app_name = 'produtos'

# PROCURANDO POR TITULO
# res = []
# for item in Produto.objects.filter(titulo__contains='125'):
#   res.append(item.titulo)
# print(res)

urlpatterns = [
  path('produtos/', ProdutoListView.as_view()),
  path('estoques/', EstoqueListView.as_view()),
  path('', home_view),
  ]