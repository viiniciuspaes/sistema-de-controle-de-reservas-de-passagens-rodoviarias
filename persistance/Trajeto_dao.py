from database.DbHelper import execute_sql, search_sql
from models.Trajeto import Trajeto


def inserir_trajeto(cod_empresa, cod_municipio_dest, cod_municipio_orig, dia_semana, horario_partida,
                    horario_chegada):

    sql = "INSERT INTO Trajeto_Horario(CodEmpresa, CodMunicio, CodMunicipioDest, DiaSemana," \
          " HorarioPartida, HorarioChegada) VALUES ({},{},{},{},{},{});".\
        format(cod_empresa, cod_municipio_dest, cod_municipio_orig, dia_semana,
               horario_partida, horario_chegada)
    execute_sql(sql)


def delete_trajeto(cod_trajeto_horario):
    sql = "DELETE FROM Trajeto_Horario WHERE CodTrajetoHorario = {} ;".format(cod_trajeto_horario)
    execute_sql(sql)


def alterar_reserva(cod_trajeto_horario,cod_empresa, cod_municio, cod_municipio_dest,
                    cod_municipio_orig, dia_semana, horario_partida, horario_chegada):

    sql = "UPDATE Trajeto_Horario SET CodEmpresa = {}, CodMunicio = {}, CodMunicipioDest = {}, CodMunicipioOrig = " \
          "{}, DiaSemana = {}, HorarioPartida = {}, HorarioChegada = {} WHERE CodTrajetoHorario = {} ;".\
        format(cod_empresa, cod_municio, cod_municipio_dest, cod_municipio_orig, dia_semana, horario_partida,
               horario_chegada, cod_trajeto_horario)
    execute_sql(sql)


def buscar_trajeto(cod_traj):

    resultado = search_sql("SELECT * FROM Trajeto_Horario WHERE CodTrajetoHorario = {}".format(cod_traj))

    if len(resultado) == 0:
        return None
    else:
        coluna = resultado[0]
        trajeto = Trajeto()
        trajeto.set_cod_traj(cod_traj)
        trajeto.set_cod_empresa(coluna[1])
        trajeto.set_cod_municipio_origem(coluna[2])
        trajeto.set_cod_municipio_destino(coluna[3])
        trajeto.set_dia(coluna[4])
        trajeto.set_horario_partida(coluna[5])
        trajeto.set_horario_chegada(coluna[6])
        return trajeto


def buscar_trajetos():

    resultado = search_sql("SELECT * FROM Trajeto_Horario")

    if len(resultado) == 0:
        return None
    else:
        trajetos = []
        for coluna in resultado:
            trajeto = Trajeto()
            trajeto.set_cod_traj(coluna[0])
            trajeto.set_cod_empresa(coluna[1])
            trajeto.set_cod_municipio_origem(coluna[2])
            trajeto.set_cod_municipio_destino(coluna[3])
            trajeto.set_dia(coluna[4])
            trajeto.set_horario_partida(coluna[5])
            trajeto.set_horario_chegada(coluna[6])
            trajetos.append(trajeto)
        return trajetos
