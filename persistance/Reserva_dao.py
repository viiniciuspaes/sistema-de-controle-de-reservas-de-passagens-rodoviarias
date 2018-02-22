from database.DbHelper import execute_sql, search_sql
from models.Reserva import Reserva


def inserir_reserva(cod_traj, numero_assento, livre = 0):
    sql = "INSERT INTO ReservaAssento(CodTrajetoHorario, NumeroAssento, Livre)VALUES ({}, {}, {}});"\
        .format(cod_traj, numero_assento, livre)
    execute_sql(sql)


def delete_reserva(cod_trajeto_horario, data, numero_assento):
    sql = " DELETE FROM ReservaAssento WHERE CodTrajetoHorario = {} AND Data = {} AND NumeroAssento = {};".\
        format(cod_trajeto_horario, data, numero_assento)
    execute_sql(sql)


def alterar_reserva(cod_trajeto_horario, data, numero_assento, novo_numero, novo_livre):
    sql = "UPDATE ReservaAssento SET NumeroAssento = {}, Livre = {} WHERE CodTrajetoHorario = {} AND Data = {}" \
           " AND NumeroAssento = {};".format(novo_numero, novo_livre, cod_trajeto_horario, data, numero_assento)
    execute_sql(sql)


def buscar_reserva(cod_traj, data, numero_assento):

    resultado = search_sql("SELECT * FROM ReservaAssento WHERE CodTrajetoHorario = {} AND Data = {}"
                           " AND NumeroAssento = {}".format(cod_traj, data, numero_assento))

    if len(resultado) == 0:
        return None
    else:
        reserva = Reserva()
        reserva.set_cod_traj(cod_traj)
        reserva.set_data(resultado[0][1])
        reserva.set_numero_assento(resultado[0][2])
        reserva.set_disponibilidade(resultado[0][3])
        return reserva
