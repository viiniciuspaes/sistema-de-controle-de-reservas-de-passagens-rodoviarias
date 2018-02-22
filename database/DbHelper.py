import pymysql

server = "localhost"
user = "root"
password = ""
db_name = "Reservas"


def get_connection():
    connection = pymysql.connect(host='localhost',
                                 user=user,
                                 password=password,
                                 db=db_name,
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    return connection


def execute_sql(sql):

    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        connection.commit()

    except:
        print("Error: Não foi possível executar commando:" + sql)
        connection.rollback()

    finally:
        connection.close()


def search_sql(sql):

    connection = get_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        connection.close()
        return results

    except:
        print("Error: Não foi possível buscar os dados")
        connection.close()
        return False


def create_database():
    connection = pymysql.connect(host='localhost',
                                 user=user,
                                 password=password)
    cursor = connection.cursor()
    database = "CREATE DATABASE IF NOT EXISTS Reservas;"
    cursor.execute(database)
    connection.commit()
    connection.close()


def create_tables():
    empresa = "CREATE table IF NOT EXISTS Empresa (CodEmp INTEGER not null AUTO_INCREMENT," \
              " Nome VARCHAR(60) NOT NULL, PRIMARY KEY (codEmp)) AUTO_INCREMENT = 1;"
    execute_sql(empresa)

    municipio = "CREATE TABLE IF NOT EXISTS Municipio (CodMunicipio INTEGER NOT NULL AUTO_INCREMENT," \
                " Nome VARCHAR(60) NOT NULL , PRIMARY KEY (CodMunicipio)) AUTO_INCREMENT = 1;"
    execute_sql(municipio)

    trajeto_horario = "CREATE TABLE IF NOT EXISTS Trajeto_Horario (CodTrajetoHorario INTEGER NOT NULL AUTO_INCREMENT," \
                      " CodEmpresa INTEGER NOT NULL REFERENCES Empresa(CodEmp) ON DELETE SET NULL ," \
                      " CodMunicio INTEGER NOT NULL REFERENCES Municipio(CodMunicipio) ON DELETE CASCADE ," \
                      " CodMunicipioDest INTEGER NOT NULL REFERENCES Municipio(CodMunicipio) ON DELETE CASCADE ," \
                      " DiaSemana VARCHAR(8) NOT NULL, HorarioPartida VARCHAR(7), HorarioChegada VARCHAR(7)," \
                      " PRIMARY KEY (CodTrajetoHorario)) AUTO_INCREMENT = 1;"
    execute_sql(trajeto_horario)

    viagem = "CREATE TABLE IF NOT EXISTS Viagem( CodTrajetoHorario INTEGER NOT NULL, Data VARCHAR(7) NOT NULL ," \
             " TotalAssentosVeiculo INTEGER NOT NULL, PRIMARY KEY (CodTrajetoHorario, Data)," \
             " FOREIGN KEY (CodTrajetoHorario) REFERENCES Trajeto_Horario(CodTrajetoHorario) ON DELETE CASCADE );"
    execute_sql(viagem)

    reserva_assento = "CREATE TABLE IF NOT EXISTS ReservaAssento(CodTrajetoHorario INTEGER NOT NULL, Data VARCHAR(7)," \
                      " NumeroAssento INTEGER, Livre BOOLEAN," \
                      " PRIMARY KEY (CodTrajetoHorario, Data, NumeroAssento)," \
                      " FOREIGN KEY (CodTrajetoHorario, Data) REFERENCES Viagem(CodTrajetoHorario, Data));"

    execute_sql(reserva_assento)


def init_db():
    create_database()
    create_tables()






