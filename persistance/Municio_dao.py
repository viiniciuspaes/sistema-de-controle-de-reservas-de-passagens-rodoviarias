from database.DbHelper import execute_sql, search_sql
from models.Municipio import Municipio


def inserir_municipio(nome):
    sql = "INSERT INTO Municipio(Nome)VALUES ({});".format(nome)
    execute_sql(sql)


def delete_municipio(cod_municipio):
    sql = " DELETE FROM Municipio WHERE CodMunicipio = {};".format(cod_municipio)
    execute_sql(sql)


def alterar_municipio(novo_nome, cod_municipio):
    sql = "UPDATE Municipio SET Nome = {} WHERE CodMunicipio = {}".format(novo_nome, cod_municipio)
    execute_sql(sql)


def buscar_municipio(cod_mun):

    resultado = search_sql("SELECT * FROM Municipio WHERE CodMunicipio = {}".format(cod_mun))

    if len(resultado) == 0:
        return None
    else:
        municipio = Municipio()
        municipio.set_cod_mun(cod_mun)
        municipio.set_nome(resultado[0][1])
        return municipio


def buscar_municipios(nome):
    resultado = search_sql("SELECT * FROM Empresa WHERE Nome LIKE %{}%".format(nome))

    if len(resultado) == 0:
        return None
    else:
        municipios = []
        for coluna in resultado:
            municipio = Municipio()
            municipio.set_cod_mun(coluna[0])
            municipio.set_nome(coluna[1])
            municipios.append(municipio)
        return municipios
