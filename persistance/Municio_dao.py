from database.DbHelper import execute_sql


def inserir_municipio(nome):
    sql = "INSERT INTO Municipio(Nome)VALUES ({});".format(nome)
    execute_sql(sql)


def delete_municipio(cod_municipio):
    sql = " DELETE FROM Municipio WHERE CodMunicipio = {};".format(cod_municipio)
    execute_sql(sql)


def alterar_municipio(novo_nome, cod_municipio):
    sql = "UPDATE Municipio SET Nome = {} WHERE CodMunicipio = {}".format(novo_nome, cod_municipio)
    execute_sql(sql)