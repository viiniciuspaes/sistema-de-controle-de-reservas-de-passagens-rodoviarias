from database.DbHelper import execute_sql, search_sql
from models.Trajeto import Trajeto


def inserir_trajeto(cod_empresa, cod_municipio_dest, cod_municipio_orig, dia_semana, horario_partida,
                    horario_chegada):

    sql = "INSERT INTO Trajeto_Horario(CodEmpresa, CodMunicio, CodMunicipioDest, DiaSemana," \
          " HorarioPartida, HorarioChegada) VALUES ({},{},{},\"{}\",\"{}\",\"{}\");".\
        format(cod_empresa, cod_municipio_dest, cod_municipio_orig, dia_semana,
               horario_partida, horario_chegada)
    if execute_sql(sql):
        return True
    else:
        return False


def delete_trajeto(cod_trajeto_horario):
    sql = "DELETE FROM Trajeto_Horario WHERE CodTrajetoHorario = {} ;".format(cod_trajeto_horario)
    execute_sql(sql)


def alterar_trajeto(cod_trajeto_horario,cod_empresa, cod_municio, cod_municipio_dest,
                     dia_semana, horario_partida, horario_chegada):

    sql = "UPDATE Trajeto_Horario SET CodEmpresa = {}, CodMunicio = {}, CodMunicipioDest = {}," \
          " DiaSemana = \"{}\", HorarioPartida = \"{}\", HorarioChegada = \"{}\" WHERE CodTrajetoHorario = {} ;".\
        format(cod_empresa, cod_municio, cod_municipio_dest, dia_semana, horario_partida,
               horario_chegada, cod_trajeto_horario)
    execute_sql(sql)


def buscar_trajeto(cod_traj):

    resultado = search_sql("SELECT * FROM Trajeto_Horario WHERE CodTrajetoHorario = {}".format(cod_traj))

    if not resultado:
        return None
    if len(resultado) == 0:
        return None
    else:
        coluna = resultado[0]
        trajeto = Trajeto()
        trajeto.set_cod_traj(cod_traj)
        trajeto.set_cod_empresa(coluna['CodEmpresa'])
        trajeto.set_cod_municipio_origem(coluna['CodMunicio'])
        trajeto.set_cod_municipio_destino(coluna['CodMunicipioDest'])
        trajeto.set_dia(coluna['DiaSemana'])
        trajeto.set_horario_partida(coluna['HorarioPartida'])
        trajeto.set_horario_chegada(coluna['HorarioChegada'])
        return trajeto


def buscar_trajetos():

    resultado = search_sql("SELECT * FROM Trajeto_Horario")

    if not resultado:
        return None
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

def all_trajetos():
    resultado = search_sql("SELECT * FROM Trajeto_Horario")

    if len(resultado) == 0:
        return None
    else:
        trajetos = []
        for i in range(len(resultado)):
            trajeto = Trajeto()
            trajeto.set_cod_traj(resultado[int(i)]['CodTrajetoHorario'])
            trajeto.set_cod_empresa(resultado[int(i)]['CodEmpresa'])
            trajeto.set_cod_municipio_origem(resultado[int(i)]['CodMunicio'])
            trajeto.set_cod_municipio_destino(resultado[int(i)]['CodMunicipioDest'])
            trajeto.set_dia(resultado[int(i)]['DiaSemana'])
            trajeto.set_horario_partida(resultado[int(i)]['HorarioPartida'])
            trajeto.set_horario_chegada(resultado[int(i)]['HorarioChegada'])
            trajetos.append(trajeto)
        return trajetos