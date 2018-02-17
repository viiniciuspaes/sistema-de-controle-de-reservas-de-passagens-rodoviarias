from database.DbHelper import execute_sql


def inserir_empresa(nome):
    sql = "INSERT INTO Empresa(Nome)VALUES {};".format(nome)
    execute_sql(sql)

