from database.DbHelper import execute_sql, search_sql
from models.Viagem import Viagem


def inserir_viagem(cod_trajeto, data, assentos):
    sql = "INSERT INTO Viagem(CodTrajetoHorario, Data, TotalAssentosVeiculo) VALUES ({}, \"{}\", {});".format(
        cod_trajeto, data, assentos)
    if execute_sql(sql):
        return True
    else:
        return False


def delete_viagem(cod_traj):
    sql = " DELETE FROM Viagem WHERE CodTrajetoHorario = {};".format(cod_traj)
    execute_sql(sql)


def alterar_viagem(data, cod_traj, assentos):
    sql = "UPDATE Viagem SET Data = \"{}\", TotalAssentosVeiculo = {} WHERE CodTrajetoHorario = {}".format(data, assentos, cod_traj)
    execute_sql(sql)


def buscar_viagem(cod_traj, data):

    resultado = search_sql("SELECT * FROM Viagem WHERE CodTrajetoHorario = {} AND Data = \"{}\"".format(cod_traj, data))

    if not resultado:
        return None
    if len(resultado) == 0:
        return None
    else:
        viagem = Viagem()
        viagem.set_cod_traj(cod_traj)
        viagem.set_data(resultado[0]['Data'])
        viagem.set_assentos(resultado[0]['TotalAssentosVeiculo'])
        return viagem


def buscar_viagens(cod_traj):
    resultado = search_sql("SELECT * FROM Viagem WHERE CodTrajetoHorario LIKE %{}%".format(cod_traj))

    if not resultado:
        return None
    if len(resultado) == 0:
        return None
    else:
        viagens = []
        for coluna in resultado:
            viagem = Viagem()
            viagem.set_cod_traj(coluna[0])
            viagem.set_data(coluna[1])
            viagem.set_assentos(coluna[2])
            viagens.append(viagem)
        return viagens

def all_viagens():
    resultado = search_sql("SELECT * FROM Viagem")

    if len(resultado) == 0:
        return None
    else:
        viagens = []
        for i in range(len(resultado)):
            viagem = Viagem()
            viagem.set_cod_traj(resultado[int(i)]['CodTrajetoHorario'])
            viagem.set_data(resultado[int(i)]['Data'])
            viagem.set_assentos(resultado[int(i)]['TotalAssentosVeiculo'])
            viagens.append(viagem)
        return viagens