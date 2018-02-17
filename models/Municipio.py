class Municipio:
    def __init__(self):
        self.cod_mun = None
        self.nome = None

    def get_cod_mun(self):
        return self.cod_mun

    def get_nome(self):
        return self.nome

    def set_cod_mun(self, cod):
        self.cod_mun = cod

    def set_nome(self, nome):
        self.nome = nome