from django.urls import path
from produtos.views import ProdutoListView

urlpatterns = [
  path('produtos/', ProdutoListView.as_view())
  ]