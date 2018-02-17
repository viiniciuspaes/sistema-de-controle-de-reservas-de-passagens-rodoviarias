class Trajeto:
    def __init__(self):
        self.cod_trajeto = None
        self.cod_empresa = None
        self.cod_municipio_origem = None
        self.cod_minicipio_dest = None
        self.dia = None
        self.horario_partida = None
        self.horario_chegada = None

    def get_cod_traj(self):
        return self.cod_trajeto

    def get_cod_empresa(self):
        return self.cod_empresa

    def get_cod_municipio_origem(self):
        return self.cod_municipio_origem

    def get_cod_municipio_destino(self):
        return self.cod_minicipio_dest

    def get_dia(self):
        return self.dia

    def get_horario_partida(self):
        return self.horario_partida

    def get_horario_chegada(self):
        return self.horario_chegada

    def set_cod_traj(self, cod):
        self.cod_trajeto = cod

    def set_cod_empresa(self, cod ):
        self.cod_empresa = cod

    def set_cod_municipio_origem(self, cod):
        self.cod_municipio_origem = cod

    def set_cod_municipio_destino(self, cod):
        self.cod_minicipio_dest = cod

    def set_dia(self, dia):
        self.dia = dia

    def set_horario_partida(self, horario):
        self.horario_partida = horario

    def set_horario_chegada(self, horario):
        self.horario_chegada = horario