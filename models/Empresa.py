class Empresa:
    def __init__(self):
        self.cod_emp = None
        self.nome = None

    def get_cod_emp(self):
        return self.cod_emp

    def get_nome(self):
        return self.nome

    def set_cod_emp(self, cod):
        self.cod_emp = cod

    def set_nome(self, nome):
        self.nome = nome
