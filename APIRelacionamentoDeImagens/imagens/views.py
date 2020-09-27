from rest_framework import viewsets, generics
from imagens.models import Imagem, Pessoa, PessoaImagem
from imagens.serializer import ImagemSerializer, PessoaSerializer, PessoaImagemSerializer, \
    PesquisaPessoasEmImagemSerializer


class ImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer


class PessoaViewSet(viewsets.ModelViewSet):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer


class PessoaImagemViewSet(viewsets.ModelViewSet):
    queryset = PessoaImagem.objects.all()
    serializer_class = PessoaImagemSerializer


class PesquisaPessoaEmImagem(generics.ListAPIView):
    def get_queryset(self):
        queryset = PessoaImagem.objects.filter(foto_id=self.kwargs['pk'])
        return queryset
    serializer_class = PesquisaPessoasEmImagemSerializer


