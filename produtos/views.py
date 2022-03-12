from django.shortcuts import render
from django.views.generic import ListView
from produtos.models import Produto, Estoque

class ProdutoListView(ListView):
  model = Produto

class EstoqueListView(ListView):
  model = Estoque

def home_view(request):
  return render(request, 'home.html')