class Tenis:
    def __init__(self, nome, quantidade, preco,cor,marca,qualidade):
        self.__nome = nome
        self.__quantidade = quantidade
        self.__preco = preco
        self.__cor = cor
        self.__marca = marca
        self.__qualidade = qualidade

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, valor):
        self.__quantidade = valor