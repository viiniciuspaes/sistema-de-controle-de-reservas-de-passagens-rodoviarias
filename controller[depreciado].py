from persistance.Empresa_dao import buscar_empresa, inserir_empresa, delete_empresa
from persistance.Municio_dao import buscar_municipio, inserir_municipio, delete_municipio
from persistance.Reserva_dao import buscar_reserva, inserir_reserva, delete_reserva
from persistance.Trajeto_dao import buscar_trajeto, inserir_trajeto, delete_trajeto
from persistance.Viagem_dao import buscar_viagem, inserir_viagem, delete_viagem


def create_empresa(empresa):
    if buscar_empresa(empresa.get_cod_emp()):
        return False
    else:
        inserir_empresa(empresa.get_nome())
        return True


def create_municipio(municipio):
    if buscar_municipio(municipio.get_cod_mun()):
        return False
    else:
        inserir_municipio(municipio.get_nome())
        return True


def create_trajeto(trajeto):
    if buscar_trajeto(trajeto.get_cod_traj()):
        return False
    else:
        inserir_trajeto(trajeto.get_cod_empresa(), trajeto.get_cod_municipio_destino(), trajeto.get_cod_municipio_origem()
                        , trajeto.get_dia(), trajeto.get_horario_partida(), trajeto.get_horario_chegada())
        return True


def create_reserva(reserva):
    if buscar_reserva(reserva.get_cod_traj(), reserva.get_data(), reserva.get_numero_assento()):
        return False
    else:
        inserir_reserva(reserva.get_cod_traj, reserva.get_numero_assento())
        return True


def create_viagem(viagem):
    if buscar_viagem(viagem.get_cod_traj(), viagem.get_data()):
        return False
    else:
        inserir_viagem(viagem.get_cod_traj(), viagem.get_data(), viagem.get_qt_assentos())
        return True


def get_viagem(viagem):
    return buscar_viagem(viagem.get_cod_traj(), viagem.get_data())


def get_reserva(reserva):
    return buscar_reserva(reserva.get_cod_traj(), reserva.get_data(), reserva.get_numero_assento())


def get_trajeto(trajeto):
    return buscar_trajeto(trajeto.get_cod_traj())


def get_municipio(municipio):
    return buscar_municipio(municipio.get_cod_mun())


def get_empresa(empresa):
    return buscar_empresa(empresa.get_cod_emp())


def delete_emp(empresa):
    delete_empresa(empresa.get_cod_emp())


def delete_mun(municipio):
    delete_municipio(municipio.get_cod_mun())


def delete_res(reserva):
    delete_reserva(reserva.get_cod_traj(), reserva.get_data(), reserva.get_numero_assento())

def delete_trajo(trajeto):
    delete_trajeto(trajeto.get_cod_traj())

def delete_viag(viagem):
    delete_viagem(viagem.get_cod_traj())
