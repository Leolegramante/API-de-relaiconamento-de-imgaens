from django.contrib import admin
from imagens.models import Imagem, Pessoa, PessoaImagem


class Imagens(admin.ModelAdmin):
    list_display = ('id', 'foto', 'descricao', 'data')
    list_display_links = ('id', 'descricao')


admin.site.register(Imagem, Imagens)


class Pessoas(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id',)


admin.site.register(Pessoa, Pessoas)


class PessoaImagens(admin.ModelAdmin):
    list_display = ('id', 'foto', 'pessoa')
    list_display_links = ('id',)


admin.site.register(PessoaImagem, PessoaImagens)
