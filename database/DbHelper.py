#utf-8
import pymysql
import time

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
        return False

    finally:
        connection.close()
        return True


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
    try:
        cursor.execute(database)
        connection.commit()
        connection.close()
    except:
        pass


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
                      " DiaSemana VARCHAR(8) NOT NULL, HorarioPartida VARCHAR(5), HorarioChegada VARCHAR(5)," \
                      " PRIMARY KEY (CodTrajetoHorario)) AUTO_INCREMENT = 1;"
    execute_sql(trajeto_horario)

    viagem = "CREATE TABLE IF NOT EXISTS Viagem( CodTrajetoHorario INTEGER NOT NULL, Data VARCHAR(8) NOT NULL ," \
             " TotalAssentosVeiculo INTEGER NOT NULL, PRIMARY KEY (CodTrajetoHorario, Data)," \
             " FOREIGN KEY (CodTrajetoHorario) REFERENCES Trajeto_Horario(CodTrajetoHorario) ON DELETE CASCADE );"
    execute_sql(viagem)

    reserva_assento = "CREATE TABLE IF NOT EXISTS ReservaAssento(CodTrajetoHorario INTEGER NOT NULL, Data VARCHAR(8)," \
                      " NumeroAssento INTEGER, Livre BOOLEAN," \
                      " PRIMARY KEY (CodTrajetoHorario, Data, NumeroAssento)," \
                      " FOREIGN KEY (CodTrajetoHorario, Data) REFERENCES Viagem(CodTrajetoHorario, Data));"

    execute_sql(reserva_assento)
def povoar():
    povoar_sql = """INSERT INTO Empresa(CodEmp, Nome)VALUES
  (1, "Gol"),
  (2, "BlueAirlines"),
  (3, "AirCanada"),
  (4, "Tan"),
  (5, "singapuraAirlines")
;
INSERT INTO municipio(CodMunicipio, Nome) VALUES
  (1, "Recife"),
  (2, "SaoPaulo"),
  (3, "Rio"),
  (4, "Vitoria"),
  (5, "Salvador")
;
INSERT INTO trajeto_horario(CodTrajetoHorario, CodEmpresa, CodMunicio, CodMunicipioDest, DiaSemana, HorarioPartida, HorarioChegada) VALUES
  (1, 1, 1, 2, "SEG", "00:30", "03:30"),
  (2, 2, 3, 4, "TER", "00:30", "03:30"),
  (3, 3, 4, 5, "SEX", "00:30", "03:30"),
  (4, 4, 5, 1, "SEG", "00:30", "03:30"),
  (5, 5, 1, 2, "SEG", "00:30", "03:30")
;
INSERT INTO viagem(CodTrajetoHorario, Data, TotalAssentosVeiculo) VALUES
  (1, "01/01/01", 10),
  (2, "01/01/01", 10),
  (3, "01/01/01", 10),
  (4, "01/01/01", 10),
  (5, "01/01/01", 10)
;
INSERT INTO reservaassento (CodTrajetoHorario, Data, NumeroAssento, Livre) VALUES
  (1, "01/01/01", 1, 0),
  (2, "01/01/01", 2, 0),
  (3, "01/01/01", 3, 0),
  (3, "01/01/01", 4, 0),
  (5, "01/01/01", 5, 0)
;"""
    execute_sql(povoar_sql)


def init_db():
    try:
        create_database()
    except Warning:
        pass
    time.sleep(3)
    create_tables()
    time.sleep(3)
    povoar()
