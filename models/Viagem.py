class Viagem:
    def __init__(self):
        self.cod_trajeto = None
        self.data = None
        self.assentos = None

    def get_cod_traj(self):
        return self.cod_trajeto

    def get_data(self):
        return self.data

    def get_qt_assentos(self):
        return self.assentos

    def set_cod_traj(self, cod):
        self.cod_trajeto = cod

    def set_data(self, data):
        self.data = data

    def set_assentos(self, number):
        self.assentos = number
