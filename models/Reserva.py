class Reserva:
    def __init__(self):
        self.cod_trajetoria = None
        self.data = None
        self.numero_assento = None
        self.disponivel = True

    def get_cod_traj(self):
        return self.cod_trajetoria

    def get_data(self):
        return self.data

    def get_numero_assento(self):
        return self.numero_assento

    def is_disponivel(self):
        if self.disponivel: return "Sim"
        else: return "Não"

    def set_disponivel(self):
        self.disponivel = True

    def set_indisponivel(self):
        self.disponivel = False

    def set_disponibilidade(self, disponibilidade):
        self.disponivel = disponibilidade

    def set_cod_traj(self, cod):
        self.cod_trajetoria = cod

    def set_data(self, data):
        self.data = data

    def set_numero_assento(self, numero):
        self.numero_assento = numero
