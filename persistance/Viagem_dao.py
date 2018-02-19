from database.DbHelper import execute_sql, search_sql
from models.Viagem import Viagem


def inserir_viagem(cod_trajeto, data, assentos):
    sql = "INSERT INTO Viagem(CodTrajetoHorario, Data, TotalAssentosVeiculo) VALUES ({}, {}, {});".format(
        cod_trajeto, data, assentos)
    execute_sql(sql)


def delete_viagem(cod_traj):
    sql = " DELETE FROM Viagem WHERE CodTrajetoHorario = {};".format(cod_traj)
    execute_sql(sql)


def alterar_viagem(data, cod_traj, assentos):
    sql = "UPDATE Viagem SET Data = {}, TotalAssentosVeiculo = {} WHERE CodEmp = {}".format(data, assentos, cod_traj)
    execute_sql(sql)


def buscar_viagem(cod_traj, data):

    resultado = search_sql("SELECT * FROM Viagem WHERE CodTrajetoHorario = {} AND Data = {}".format(cod_traj, data))

    if len(resultado) == 0:
        return None
    else:
        viagem = Viagem()
        viagem.set_cod_traj(cod_traj)
        viagem.set_data(resultado[0][1])
        viagem.set_assentos(resultado[0][2])
        return viagem


def buscar_viagens(cod_traj):
    resultado = search_sql("SELECT * FROM Viagem WHERE CodTrajetoHorario LIKE %{}%".format(cod_traj))

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
