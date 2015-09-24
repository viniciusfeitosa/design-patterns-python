# -*- coding: UTF-8 -*-
from datetime import date
from observadores import imprime, envia_por_email, salva_no_banco


class Item(object):
    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor


class NotaFiscal(object):
    def __init__(
            self,
            razao_social,
            cnpj,
            itens,
            detalhes="",
            data_de_emissao=date.today(),
            observadores=[]):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if len(detalhes) > 20:
            raise Exception(
                'Detalhes da nota não pode ter mais do que 20 caracteres')
        self.__detalhes = detalhes
        self.__itens = itens
        for observador in observadores:
            observador(self)

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes

    @property
    def itens(self):
        return self.__itens

if __name__ == '__main__':

    from criado_de_nota_fiscal import CriadorDeNotaFiscal

    itens = [
        Item('ITEM A', 100),
        Item('ITEM B', 200),
    ]

    nota_fiscal = NotaFiscal(
        razao_social='FHSA Limitada',
        cnpj='012345678901234',
        itens=itens,
        data_de_emissao=date.today(),
        detalhes='Um teste',
        observadores=[imprime, envia_por_email, salva_no_banco]
        )
