from database.DbHelper import init_db, get_connection
from persistance.Empresa_dao import buscar_empresa, inserir_empresa, delete_empresa, all_empresas, alterar_empresa
from persistance.Municio_dao import buscar_municipio, inserir_municipio, delete_municipio, all_municipios, alterar_municipio
from persistance.Reserva_dao import buscar_reserva, inserir_reserva, delete_reserva, all_reservas, alterar_reserva
from persistance.Trajeto_dao import buscar_trajeto, inserir_trajeto, delete_trajeto, all_trajetos, alterar_trajeto
from persistance.Viagem_dao import buscar_viagem, inserir_viagem, delete_viagem, all_viagens, alterar_viagem
import warnings

warnings.filterwarnings('ignore')


def create_empresa(empresa):
    if inserir_empresa(empresa):
        return True
    else:
        return False

def create_municipio(municipio):
    if inserir_municipio(municipio):
        return True
    else:
        return False


def create_trajeto(cod_empresa, cod_municipio_dest, cod_municipio_orig, dia_semana,
               horario_partida, horario_chegada):
    if inserir_trajeto(cod_empresa, cod_municipio_dest, cod_municipio_orig, dia_semana,
               horario_partida, horario_chegada):

        return True
    else:
        return False


def create_reserva(codigo, data, assento, disponibilidade):
    if (buscar_viagem(codigo,data)):
        if buscar_viagem(codigo,data).get_qt_assentos() >= int(assento):
            if int(assento) <= 0:
                print("Assento nao existe")
                return False
            else:
                if inserir_reserva(codigo, data, assento, disponibilidade):
                    return True
                else:
                    return False
        else:
            print("Assento não existe.\n")
            return False
    else:
        print("Viagem e/ou Data não existe(m).\n")
        return False


def create_viagem(cod_trajeto, data, assentos):
    if buscar_viagem(cod_trajeto, data):
        return False
    else:
        if get_trajeto(codigo):
            if inserir_viagem(cod_trajeto, data, assentos):
                return True
            else:
                return False
        else:
            print("Código Trajeto não existe.\n")
            return False


def get_viagem(codigo,data):
    return buscar_viagem(codigo,data)


def get_reserva(codigo,data,assento):
    return buscar_reserva(codigo,data,assento)


def get_trajeto(trajeto):
    return buscar_trajeto(trajeto)


def get_municipio(municipio):
    return buscar_municipio(municipio)


def get_empresa(empresa):
    return buscar_empresa(empresa)


def delete_emp(empresa):
    delete_empresa(empresa)


def delete_mun(municipio):
    delete_municipio(municipio)


def delete_res(codigo,data,assento):
    delete_reserva(codigo,data,assento)


def delete_trajo(trajeto):
    delete_trajeto(trajeto)


def delete_viag(viagem):
    delete_viagem(viagem)


if __name__ == '__main__':

    print("Sistema de Cadastro de Reservas\n")
    print("Criando database...")
    init_db()
    print("Schema e tabelas criadas!\n")
    print("=====================================================================================================")
    acao = input("READ Empresa:1\t\t READ Município:2\t\t READ Trajeto:3\t\t READ Reserva:4\t\t READ Viagem:5\n"
                 "CREATE Empresa:6\t\t CREATE Município:7\t\t CREATE Trajeto:8\t\t CREATE Reserva:9\t\t CREATE Viagem:10\n"
                 "DEL Empresa:11\t\t DEL Município:12\t\t DEL Trajeto:13\t\t DEL Reserva:14\t\t DEL Viagem:15\n"
                 "LIST Empresas:16\t\t LIST Municípios:17\t\t LIST Trajetos:18\t\t LIST Reservas:19\t\t LIST Viagens:20\n"
                 "ALTER Empresa:21\t\t ALTER Município:22\t\t ALTER Trajeto:23\t\t ALTER Reserva:24\t\t ALTER Viagem:25\n"
                 "SAIR: 0\n\n"
                 "Digite o valor correspondente à ação desejada: \n")
    while acao != 0:
        try:
            acao = int(acao)
            while acao not in range(26):
                acao = int(input("Valor inválido. Tente novamente\n"))
        except:
            acao = input("Valor inválido. Tente novamente\n")

        if type(acao)==int and acao <16 and acao>0: print("Digite os dados:")

        if acao == 1:
            codigo = input("Código: ")
            empresa = get_empresa(codigo)
            if empresa:
                print("\nEmpresa:\nCódigo: "+empresa.get_cod_emp(),"\tNome: "+empresa.get_nome()+"\n")
            else:
                print("Empresa não existe.\n")

        elif acao == 2:
            codigo = input("Código: ")
            municipio = get_municipio(codigo)
            if municipio:
                print("\nMunicípio:\nCódigo: " + municipio.get_cod_mun(), "\tNome: " + municipio.get_nome() + "\n")
            else:
                print("Município não existe.\n")

        elif acao == 3:
            codigo = input("Código: ")
            trajeto = get_trajeto(codigo)
            if trajeto:
                empresa = get_empresa(trajeto.get_cod_empresa()).get_nome()
                origem = get_municipio(trajeto.get_cod_municipio_origem()).get_nome()
                destino = get_municipio(trajeto.get_cod_municipio_destino()).get_nome()

                print("\nTrajeto:\nCódigo: " + trajeto.get_cod_traj(), "\tEmpresa: " + empresa,
                      "\nOrigem: " + origem, "\t\tDestino: " + destino, "\nDia da Semana: " + trajeto.get_dia(),
                      "\t\tHorário Partida: " + trajeto.get_horario_partida(), "\t\t Horário Chegada: " + trajeto.get_horario_chegada() + "\n")
            else:
                print("Trajeto não existe.\n")
        elif acao == 4:
            codigo = input("Código Trajeto: ")
            data = input("Data (dd/mm/aa): ")
            assento = input("Assento: ")
            reserva = get_reserva(codigo,data,assento)
            if reserva:
                print("\nReserva:\nCódigo Trajeto: " + reserva.get_cod_traj(), "\tData: " + reserva.get_data(),
                      "\t\tnº Assento: " + str(reserva.get_numero_assento()), "\t\tDisponível: "+ reserva.is_disponivel() + "\n")
            else:
                print("Rserva não existe.\n")
        elif acao == 5:
            codigo = input("Código Trajeto: ")
            data = input("Data (dd/mm/aa): ")
            viagem = get_viagem(codigo,data)
            if viagem:
                print("\nViagem:\nCódigo Trajeto: " + viagem.get_cod_traj(), "\tData: " + viagem.get_data(),
                      "\t\tTotal Assentos: " + str(viagem.get_qt_assentos()) + "\n")
            else:
                print("Viagem não existe.\n")
        elif acao == 6:
            nome = input("Nome: ")
            if create_empresa(nome): print("Empresa criada com sucesso!\n")
            else: print("Não foi possível criar a empresa.\n")
        elif acao == 7:
            nome = input("Nome: ")
            if create_municipio(nome): print("Município criado com sucesso!\n")
            else: print("Não foi possível criar o município.\n")
        elif acao == 8:
            cod_empresa = input("Código Empresa: ")
            cod_municipio_dest = input("Código Município Destino: ")
            cod_municipio_orig = input("Código Município Origem: ")
            dia_semana = input("Dia da Semana (SEG,TER,QUAR,QUIN,SEX,SAB ou DOM): ")
            horario_partida = input("Horário Partida (hh:mm): ")
            horario_chegada = input("Horário Chegada (hh:mm): ")
            if create_trajeto(cod_empresa, cod_municipio_dest, cod_municipio_orig, dia_semana,
               horario_partida, horario_chegada): print("Trajeto criado com sucesso!\n")
            else:print("Não foi possível criar o Trajeto.\n")

        elif acao == 9:
            codigo = input("Código Trajeto: ")
            data = input("Data (dd/mm/aa): ")
            assento = input("Assento: ")
            disponibilidade = input("Disponibilidade Livre/Não (1 ou 0): ")
            if create_reserva(codigo, data, assento, disponibilidade):
                print("Reserva criada com sucesso!\n")
            else:
                print("Não foi possível criar a reserva.\n")
        elif acao == 10:
            codigo = input("Código Trajeto: ")
            data = input("Data (dd/mm/aa): ")
            assento = input("Total Assentos: ")
            if create_viagem(codigo,data,assento):
                print("Viagem criada com sucesso!\n")
            else:
                print("Não foi possível criar a viagem.\n")
        elif acao == 11:
            codigo = input("Código: ")
            delete_emp(codigo)
            print("Empresa excluída.\n")
        elif acao == 12:
            codigo = input("Código: ")
            delete_mun(codigo)
            print("Município excluído.\n")
        elif acao == 13:
            codigo = input("Código: ")
            delete_trajo(codigo)
            print("Trajeto excluído.\n")
        elif acao == 14:
            codigo = input("Código: ")
            data = input("Data: ")
            assento = input("Assento: ")
            delete_res(codigo,data,assento)
            print("Reserva excluída.\n")
        elif acao == 15:
            codigo = input("Código: ")
            delete_viag(codigo)
            print("Viagem excluída.\n")
        elif acao == 16:
            empresas = all_empresas()
            if not empresas:
                print("Não há empresas.\n")
            else:
                print("Empresas (Código Nome):\n")
                for empresa in empresas:
                    print(empresa.get_cod_emp(),empresa.get_nome())
                print()
        elif acao == 17:
            municipios = all_municipios()
            if not municipios:
                print("Não há municípios.\n")
            else:
                print("Municípios (Código Nome):\n")
                for municipio in municipios:
                    print(municipio.get_cod_mun(),municipio.get_nome())
                print()
        elif acao == 18:
            trajetos = all_trajetos()
            if not trajetos:
                print("Não há trajetos.\n")
            else:
                print("Trajetos (Código CódigoEmpresa CódigoMunicípioOrigem CódigoMunicípioDestino"
                      " DiaSemana HorárioPartida HorárioChegada):\n")
                for trajeto in trajetos:
                    print(trajeto.get_cod_traj(),trajeto.get_cod_empresa(),trajeto.get_cod_municipio_origem(),
                          trajeto.get_cod_municipio_destino(),trajeto.get_dia(),trajeto.get_horario_partida(),
                          trajeto.get_horario_chegada())
                print()
        elif acao == 19:
            reservas = all_reservas()
            if not reservas:
                print("Não há reservas.\n")
            else:
                print("Reservas (CódigoTrajeto Data NumeroAssento Livre):\n")
                for reserva in reservas:
                    print(reserva.get_cod_traj(),reserva.get_data(),reserva.get_numero_assento(),reserva.is_disponivel())
                print()
        elif acao == 20:
            viagens = all_viagens()
            if not viagens:
                print("Não há viagens.\n")
            else:
                print("Viagens (CódigoTrajeto Data TotalAssentos):\n")
                for viagem in viagens:
                    print(viagem.get_cod_traj(),viagem.get_data(),viagem.get_qt_assentos())
                print()
        elif acao == 21:
            codigo = input("Código: ")
            nome = input("Novo nome: ")
            alterar_empresa(nome, codigo)
            print("Empresa alterada.\n")
        elif acao == 22:
            codigo = input("Código: ")
            nome = input("Novo nome: ")
            alterar_municipio(nome, codigo)
            print("Município alterado.\n")

        elif acao == 23:
            cod_trajeto_horario = input("Código Trajeto: ")
            print("Caso não deseje alterar os dados a seguir digite o valor antigo!")
            cod_empresa = input("Novo Código Empresa: ")
            cod_municio = input("Novo Código Município Origem: ")
            cod_municipio_dest = input("Novo Código Município Destino: ")
            dia_semana = input("Novo Dia da Semana (SEG,TER,QUAR,QUIN,SEX,SAB ou DOM): ")
            horario_partida = input("Novo Horário Partida (hh:mm): ")
            horario_chegada = input("Novo Horário Chegada (hh:mm): ")
            alterar_trajeto(cod_trajeto_horario, cod_empresa, cod_municio, cod_municipio_dest,
                            dia_semana, horario_partida, horario_chegada)
            print("Trajeto alterado.\n")
        elif acao == 24:
            codigo = input("Código Trajeto: ")
            data = input("Data (dd/mm/aa): ")
            numero_assento = input("nº Assento: ")
            print("Caso não deseje alterar os dados a seguir digite o valor antigo!")
            novo_numero = input("Novo nº Assento: ")
            novo_livre = input("Nova Disponibilidade Livre/Não (1/0):")
            alterar_reserva(codigo, data, numero_assento, novo_numero, novo_livre)
            print("Reserva alterada.\n")
        elif acao == 25:
            codigo = input("Código Trajeto: ")
            print("Caso não deseje alterar os dados a seguir digite o valor antigo!")
            data = input("Nova Data (dd/mm/aa): ")
            assentos = input("Novo nº Assentos: ")
            alterar_viagem(data, codigo, assentos)
            print("Viagem alterada.\n")
        elif acao==0:
            break

        acao = input("Digite uma nova ação desejada: \n")

