from rest_framework import serializers
from imagens.models import Imagem, Pessoa, PessoaImagem


class ImagemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Imagem
        fields = '__all__'


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = '__all__'


class PessoaImagemSerializer(serializers.ModelSerializer):
    foto = serializers.ReadOnlyField(source='foto.descricao')
    pessoa = serializers.ReadOnlyField(source='pessoa.nome')

    class Meta:
        model = PessoaImagem
        fields = ['foto', 'pessoa']


class PesquisaPessoasEmImagemSerializer(serializers.ModelSerializer):
    foto = serializers.ReadOnlyField(source='foto.descricao')
    pessoa = serializers.ReadOnlyField(source='pessoa.nome')

    class Meta:
        model = PessoaImagem
        fields = ['foto', 'pessoa']