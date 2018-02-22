from database.DbHelper import init_db, get_connection
from persistance.Empresa_dao import buscar_empresa, inserir_empresa, delete_empresa
from persistance.Municio_dao import buscar_municipio, inserir_municipio, delete_municipio
from persistance.Reserva_dao import buscar_reserva, inserir_reserva, delete_reserva
from persistance.Trajeto_dao import buscar_trajeto, inserir_trajeto, delete_trajeto
from persistance.Viagem_dao import buscar_viagem, inserir_viagem, delete_viagem
from tkinter import*
import tkinter.ttk as ttk

init_db()
root = Tk()
root.title("Sistema de Cadastro de Reservas")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 1500
height = 550
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

# ==================================VARIABLES==========================================
empresa_nome = StringVar()
municipio_nome = StringVar()
municipio_origem = StringVar()
municipio_destino = StringVar()
total_assentos = IntVar()
data = StringVar()
cod_emp = IntVar()
cod_minicipio = IntVar()
cod_traj = IntVar()

# ==================================FRAME==============================================
Top = Frame(root, width=1300, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
Left = Frame(root, width=300, height=500, bd=8)
Left.pack(side=LEFT)
Right = Frame(root, width=300, height=500, bd=8)
Right.pack(side=RIGHT)
Midle = Frame(root, width=300, height=500, bd=8)
Midle.pack(side=LEFT)
Forms = Frame(Left, width=300, height=500)
Forms.pack(side=TOP)
Forms2 = Frame(Midle, width=300, height=500)
Forms2.pack(side=TOP)
Buttons = Frame(Left, width=300, height=100, bd=8, )
Buttons.pack(side=BOTTOM)
Buttons2 = Frame(Midle, width=300, height=100, bd=8, )
Buttons.pack(side=BOTTOM)


# ==================================LABEL WIDGET=======================================
txt_title = Label(Top, width=900, font=('arial', 12), text="Sistema de Cadastro de Reservas")
txt_title.pack()
txt_empresa_nome = Label(Forms, text="Empresa:", font=('arial', 11), bd=15)
txt_empresa_nome.grid(row=0, stick="e")
txt_minicipio_nome = Label(Forms, text="Municipio:", font=('arial', 11), bd=15)
txt_minicipio_nome.grid(row=1, stick="e")
txt_municipio_origem = Label(Forms, text="Origem:", font=('arial', 11), bd=15)
txt_municipio_origem.grid(row=2, stick="e")
txt_mmunicipio_destino = Label(Forms, text="Destino:", font=('arial', 11), bd=15)
txt_mmunicipio_destino.grid(row=3, stick="e")
txt_total_assentos = Label(Forms, text="Total Assentos:", font=('arial', 11), bd=15)
txt_total_assentos.grid(row=4, stick="e")
txt_data = Label(Forms, text="data:", font=('arial', 11), bd=15)
txt_data.grid(row=5, stick="e", )
txt_cod_emp = Label(Forms, text="cod_emp",  font=('arial', 11), bd=15)
txt_cod_emp.grid(row=6, stick="e")
txt_cod_mun = Label(Forms, text="cod_mun",  font=('arial', 11), bd=15)
txt_cod_mun.grid(row=7, stick="e")
txt_cod_traj = Label(Forms, text='Cod_traj',  font=('arial', 11), bd=15)
txt_cod_traj.grid(row=8, stick="e")

txt_empresa_nome2 = Label(Forms2, text="Empresa:", font=('arial', 11), bd=15)
txt_empresa_nome2.grid(row=0, stick="e")
txt_minicipio_nome2 = Label(Forms2, text="Municipio:", font=('arial', 11), bd=15)
txt_minicipio_nome2.grid(row=1, stick="e")
txt_municipio_origem2 = Label(Forms2, text="Origem:", font=('arial', 11), bd=15)
txt_municipio_origem2.grid(row=2, stick="e")
txt_mmunicipio_destino2 = Label(Forms2, text="Destino:", font=('arial', 11), bd=15)
txt_mmunicipio_destino2.grid(row=3, stick="e")
txt_total_assentos2 = Label(Forms2, text="Total Assentos:", font=('arial', 11), bd=15)
txt_total_assentos2.grid(row=4, stick="e")
txt_data2 = Label(Forms2, text="data:", font=('arial', 11), bd=15)
txt_data2.grid(row=5, stick="e", )
txt_cod_emp2 = Label(Forms2, text="cod_emp",  font=('arial', 11), bd=15)
txt_cod_emp2.grid(row=6, stick="e")
txt_cod_mun2 = Label(Forms2, text="cod_mun",  font=('arial', 11), bd=15)
txt_cod_mun2.grid(row=7, stick="e")
txt_cod_traj2 = Label(Forms2, text='Cod_traj',  font=('arial', 11), bd=15)
txt_cod_traj2.grid(row=8, stick="e")

# ==================================ENTRY WIDGET=======================================
et_empresa_nome = Entry(Forms, textvariable=empresa_nome, width=30)
et_empresa_nome.grid(row=0, column=1)
et_minicipio_nome = Entry(Forms, textvariable=municipio_nome, width=30)
et_minicipio_nome.grid(row=1, column=1)
et_origem = Entry(Forms, textvariable=municipio_origem, width=30)
et_origem.grid(row=2, column=1)
et_destino = Entry(Forms, textvariable=municipio_destino, width=30)
et_destino.grid(row=3, column=1)
et_total_assentos = Entry(Forms, textvariable=total_assentos, width=30)
et_total_assentos.grid(row=4, column=1)
et_data = Entry(Forms, textvariable=data, show="*", width=30)
et_data.grid(row=5, column=1)

et_empresa_nome_2 = Entry(Forms2, textvariable=empresa_nome, width=30)
et_empresa_nome_2.grid(row=0, column=1)
et_municipio_nome_2 = Entry(Forms2, textvariable=municipio_nome, width=30)
et_municipio_nome_2.grid(row=1, column=1)
et_origem_2 = Entry(Forms2, textvariable=municipio_origem, width=30)
et_origem_2.grid(row=2, column=1)
et_destino_2 = Entry(Forms2, textvariable=municipio_destino, width=30)
et_destino_2.grid(row=3, column=1)
et_total_assentos_2 = Entry(Forms2, textvariable=total_assentos, width=30)
et_total_assentos_2.grid(row=4, column=1)
et_data_2 = Entry(Forms2, textvariable=data, show="*", width=30)
et_data_2.grid(row=5, column=1)

#------------------------------------FUNCTIONS---------------------------------
# TODO: controller functions should be here

# TODO: THERE IS NOT NEED TO USER MODEL ANYMORE, you can pass the value directly to the DB, the return can be model oriented
"""
os buscar ainda retornam objetos ent na hora de passar para as arvores e preciso pegar os valores dos objetos"""

def create_empresa(empresa): #TODO: modificar o atributo do metodo para nao receber mais um objeto e sim a string direta
    if buscar_empresa(empresa.get_cod_emp()):
        return False
    else:
        inserir_empresa(empresa.get_nome())
        return True


def create_municipio(municipio):
    if buscar_municipio(municipio.get_cod_mun()):
        return False
    else:
        inserir_municipio(municipio.get_nome())
        return True


def create_trajeto(trajeto):
    if buscar_trajeto(trajeto.get_cod_traj()):
        return False
    else:
        inserir_trajeto(trajeto.get_cod_empresa(), trajeto.get_cod_municipio_destino(), trajeto.get_cod_municipio_origem()
                        , trajeto.get_dia(), trajeto.get_horario_partida(), trajeto.get_horario_chegada())
        return True


def create_reserva(reserva):
    if buscar_reserva(reserva.get_cod_traj(), reserva.get_data(), reserva.get_numero_assento()):
        return False
    else:
        inserir_reserva(reserva.get_cod_traj, reserva.get_numero_assento())
        return True


def create_viagem(viagem):
    if buscar_viagem(viagem.get_cod_traj(), viagem.get_data()):
        return False
    else:
        inserir_viagem(viagem.get_cod_traj(), viagem.get_data(), viagem.get_qt_assentos())
        return True


def get_viagem(viagem):
    return buscar_viagem(viagem.get_cod_traj(), viagem.get_data())


def get_reserva(reserva): #TODO: a medida que os metodos tenham mais coisas sendo usadas modificar para a string equivalente
    return buscar_reserva(reserva.get_cod_traj(), reserva.get_data(), reserva.get_numero_assento())


def get_trajeto(trajeto):
    return buscar_trajeto(trajeto.get_cod_traj())


def get_municipio(municipio):
    return buscar_municipio(municipio.get_cod_mun())


def get_empresa(empresa):
    return buscar_empresa(empresa.get_cod_emp())


def delete_emp(empresa):
    delete_empresa(empresa.get_cod_emp())


def delete_mun(municipio):
    delete_municipio(municipio.get_cod_mun())


def delete_res(reserva):
    delete_reserva(reserva.get_cod_traj(), reserva.get_data(), reserva.get_numero_assento())

def delete_trajo(trajeto):
    delete_trajeto(trajeto.get_cod_traj())

def delete_viag(viagem):
    delete_viagem(viagem.get_cod_traj())

def all_empresas(): #TODO: all para cada classe
    tree.delete(*tree.get_children())
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM `Empresa` ORDER BY `Nome` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[1], data[2], data[3], data[4], data[5], data[6]))
    cursor.close()
    connection.close()
    t

# ==================================BUTTONS WIDGET=====================================
btn_create = Button(Buttons, width=10, text="Create", command=DISABLED)
btn_create.pack(side=LEFT)
btn_read = Button(Buttons, width=10, text="Read", command=DISABLED)
btn_read.pack(side=LEFT)
btn_update = Button(Buttons, width=10, text="Update", state=DISABLED)
btn_update.pack(side=LEFT)
btn_delete = Button(Buttons, width=10, text="Delete", state=DISABLED)
btn_delete.pack(side=LEFT)
btn_exit = Button(Buttons, width=10, text="Exit", command=DISABLED)
btn_exit.pack(side=LEFT)

btn_create2 = Button(Buttons2, width=10, text="Create", command=DISABLED)
btn_create2.pack(side=LEFT)
btn_read2 = Button(Buttons2, width=10, text="Read", command=DISABLED)
btn_read2.pack(side=LEFT)
btn_update2 = Button(Buttons2, width=10, text="Update", state=DISABLED)
btn_update2.pack(side=LEFT)
btn_delete2 = Button(Buttons2, width=10, text="Delete", state=DISABLED)
btn_delete2.pack(side=LEFT)
btn_exit2 = Button(Buttons2, width=10, text="Exit", command=DISABLED)
btn_exit2.pack(side=LEFT)

# ==================================LIST WIDGET========================================
scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
tree = ttk.Treeview(Right, columns=("Firstname", "Lastname", "Gender", "Address", "Username", "Password"),
                    selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('Firstname', text="Firstname", anchor=W)
tree.heading('Lastname', text="Lastname", anchor=W)
tree.heading('Gender', text="Gender", anchor=W)
tree.heading('Address', text="Address", anchor=W)
tree.heading('Username', text="Username", anchor=W)
tree.heading('Password', text="Password", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=80)
tree.column('#2', stretch=NO, minwidth=0, width=120)
tree.column('#3', stretch=NO, minwidth=0, width=80)
tree.column('#4', stretch=NO, minwidth=0, width=150)
tree.column('#5', stretch=NO, minwidth=0, width=120)
tree.column('#6', stretch=NO, minwidth=0, width=120)
tree.pack()



#==================================INITIALIZATION=====================================
if __name__ == '__main__':
    root.mainloop()