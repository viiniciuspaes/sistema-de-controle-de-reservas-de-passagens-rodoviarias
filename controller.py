# ---- Empresa controler ---
from persistance.Empresa_dao import buscar_empresa, inserir_empresa, buscar_empresas
from persistance.Municio_dao import buscar_municipios


def create_empresa(empresa):
    if len(buscar_empresas(empresa.get_nome())) > 0:
        return False
    else:
        inserir_empresa(empresa.get_nome())
        return True


def create_municipio(municipio):
    if len(buscar_municipios(municipio.get_nome())):
        return False
