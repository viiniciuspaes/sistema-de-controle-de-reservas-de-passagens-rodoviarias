from database.DbHelper import execute_sql, search_sql
from models.Reserva import Reserva


def inserir_reserva(cod_traj, data, numero_assento, livre = 0):
    sql = "INSERT INTO ReservaAssento(CodTrajetoHorario, Data, NumeroAssento, Livre)VALUES ({},\"{}\", {}, {});"\
        .format(cod_traj, data, numero_assento, livre)
    if execute_sql(sql):
        return True
    else:
        return False


def delete_reserva(cod_trajeto_horario, data, numero_assento):
    sql = " DELETE FROM ReservaAssento WHERE CodTrajetoHorario = {} AND Data = \"{}\" AND NumeroAssento = {};".\
        format(cod_trajeto_horario, data, numero_assento)
    execute_sql(sql)


def alterar_reserva(cod_trajeto_horario, data, numero_assento, novo_numero, novo_livre):
    sql = "UPDATE ReservaAssento SET NumeroAssento = {}, Livre = {} WHERE CodTrajetoHorario = {} AND Data = \"{}\"" \
           " AND NumeroAssento = {};".format(novo_numero, novo_livre, cod_trajeto_horario, data, numero_assento)
    execute_sql(sql)


def buscar_reserva(cod_traj, data, numero_assento):

    resultado = search_sql("SELECT * FROM ReservaAssento WHERE CodTrajetoHorario = {} AND Data = \"{}\""
                           " AND NumeroAssento = {}".format(cod_traj, data, numero_assento))

    if not resultado:
        return None
    if len(resultado) == 0:
        return None
    else:
        reserva = Reserva()
        reserva.set_cod_traj(cod_traj)
        reserva.set_data(resultado[0]['Data'])
        reserva.set_numero_assento(resultado[0]['NumeroAssento'])
        reserva.set_disponibilidade(resultado[0]['Livre'])
        return reserva

def all_reservas():
    resultado = search_sql("SELECT * FROM ReservaAssento")

    if len(resultado) == 0:
        return None
    else:
        reservas = []
        for i in range(len(resultado)):
            reserva = Reserva()
            reserva.set_cod_traj(resultado[int(i)]['CodTrajetoHorario'])
            reserva.set_data(resultado[int(i)]['Data'])
            reserva.set_numero_assento(resultado[int(i)]['NumeroAssento'])
            reserva.set_disponibilidade(resultado[int(i)]['Livre'])
            reservas.append(reserva)
    return reservas