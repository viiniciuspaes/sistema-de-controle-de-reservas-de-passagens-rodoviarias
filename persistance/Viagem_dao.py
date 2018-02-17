from database.DbHelper import execute_sql


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
