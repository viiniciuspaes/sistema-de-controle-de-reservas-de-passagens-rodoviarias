from database.DbHelper import execute_sql, search_sql
from models.Empresa import Empresa


def inserir_empresa(nome):
    sql = "INSERT INTO Empresa(Nome)VALUES (\"{}\");".format(nome)
    if execute_sql(sql):
        return True
    else:
        False


def delete_empresa(cod_emp):
    sql = " DELETE FROM Empresa WHERE CodEmp = {};".format(cod_emp)
    execute_sql(sql)


def alterar_empresa(novo_nome, cod_emp):
    sql = "UPDATE Empresa SET Nome = \"{}\" WHERE CodEmp = {}".format(novo_nome, cod_emp)
    execute_sql(sql)

def buscar_empresa(cod_emp):

    resultado = search_sql("SELECT * FROM Empresa WHERE CodEmp = {}".format(cod_emp))

    if not resultado:
        return None
    if len(resultado) == 0:
        return None
    else:
        # print((resultado[0]))
        empresa = Empresa()
        empresa.set_cod_emp(cod_emp)
        empresa.set_nome(resultado[0]['Nome'])
        return empresa


def buscar_empresa_nome(nome):
    resultado = search_sql("SELECT * FROM Empresa WHERE Nome = {}".format(nome))

    if not resultado:
        return None
    if len(resultado) == 0:
        return None
    else:
        empresa = Empresa()
        empresa.set_cod_emp(resultado[0]['CodEmp'])
        empresa.set_nome(resultado[0]['Nome'])
        return empresa


def buscar_empresas(nome):
    resultado = search_sql("SELECT * FROM Empresa WHERE Nome LIKE %{}%".format(nome))

    if not resultado:
        return None
    if len(resultado) == 0:
        return None
    else:
        empresas = []
        for coluna in resultado:
            empresa = Empresa()
            empresa.set_cod_emp(coluna[0])
            empresa.set_nome(coluna[1])
            empresas.append(empresa)
        return empresas

def all_empresas():
    resultado = search_sql("SELECT * FROM Empresa")

    if len(resultado) == 0:
        return None
    else:
        empresas = []
        for i in range(len(resultado)):
            empresa = Empresa()
            empresa.set_cod_emp(resultado[int(i)]['CodEmp'])
            empresa.set_nome(resultado[int(i)]['Nome'])
            empresas.append(empresa)
        return empresas