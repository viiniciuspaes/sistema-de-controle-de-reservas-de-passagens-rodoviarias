from database.DbHelper import execute_sql


def inserir_reserva(numero_assento, livre = 0):
    sql = "INSERT INTO ReservaAssento(NumeroAssento, Livre)VALUES ({});".format(numero_assento,livre)
    execute_sql(sql)


def delete_reserva(cod_trajeto_horario, data, numero_assento):
    sql = " DELETE FROM ReservaAssento WHERE CodTrajetoHorario = {} AND Data = {} AND NumeroAssento = {};".\
        format(cod_trajeto_horario, data, numero_assento)
    execute_sql(sql)


def alterar_reserva(cod_trajeto_horario, data, numero_assento, novo_numero, novo_livre):
    sql = "UPDATE ReservaAssento SET NumeroAssento = {}, Livre = {} WHERE CodTrajetoHorario = {} AND Data = {} AND NumeroAssento = {};".\
        format(novo_numero, novo_livre, cod_trajeto_horario, data, numero_assento)
    execute_sql(sql)