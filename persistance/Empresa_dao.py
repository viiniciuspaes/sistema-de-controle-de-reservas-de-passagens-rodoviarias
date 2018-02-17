from database.DbHelper import execute_sql


def inserir_empresa(nome):
    sql = "INSERT INTO Empresa(Nome)VALUES ({});".format(nome)
    execute_sql(sql)


def delete_empresa(cod_emp):
    sql = " DELETE FROM Empresa WHERE CodEmp = {};".format(cod_emp)
    execute_sql(sql)


def alterar_empresa(novo_nome, cod_emp):
    sql = "UPDATE Empresa SET Nome = {} WHERE CodEmp = {}".format(novo_nome, cod_emp)
    execute_sql(sql)
