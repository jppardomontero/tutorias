from tkinter import *
from conexion import conexion
from tkinter import messagebox
from tkinter import ttk

def guardarProveedor():
    sql = "INSERT INTO proveedor (cedula, nombres, empresa, correo, direccion) VALUES(?,?,?,?,?)" 
    parametros = (txtCedula.get(), txtNombres.get(), txtEmpresa.get(), txtCorreo.get(), txtDireccion.get())
    if conexion.ejecutar(sql, parametros):
        messagebox.showinfo(message="Los datos del proveedor guardaos con éxito", title="Guardar datos")
        cargarProveedor()
    else:
        messagebox.showwarning(message="Los dotos no pueden ser guardados", title="Guardos datos")

def cargarProveedor():
    sql = "SELECT * FROM proveedor"
    dataProveedor = conexion.ejecutar(sql,())
    limpiarTabla = datos.get_children()
    for elemento in limpiarTabla:
        datos.delete(elemento)
    for row in dataProveedor:
        datos.insert("", row[0], values=(row[0], row[1], row[2], row[3], row[4],row[5]))



ventanaProveedor = Tk()
ventanaProveedor.title("Adminitración de proveedores")
ventanaProveedor.geometry("800x600")

framePrincipal = LabelFrame(ventanaProveedor, text="Datos de proveedor")
framePrincipal.grid(column=0, row=0)

Label(framePrincipal, text="Cédula:").grid(column=0, row=0, padx=3, pady=3, columnspan=2, sticky="NSEW")
txtCedula = Entry(framePrincipal)
txtCedula.grid(column=1, row=0, padx=3, pady=3, columnspan=2, sticky="E")

Label(framePrincipal, text="Nombres:").grid(column=0, row=1, padx=3, pady=3)
txtNombres = Entry(framePrincipal)
txtNombres.grid(column=1, row=1, padx=3, pady=3)

Label(framePrincipal, text="Empresa:").grid(column=2, row=1, padx=3, pady=3)
txtEmpresa = Entry(framePrincipal)
txtEmpresa.grid(column=3, row=1, padx=3, pady=3)

Label(framePrincipal, text="Correo:").grid(column=0, row=2, padx=3, pady=3)
txtCorreo = Entry(framePrincipal)
txtCorreo.grid(column=1, row=2, padx=3, pady=3)

Label(framePrincipal, text="Direccion:").grid(column=2, row=2, padx=3, pady=3)
txtDireccion = Entry(framePrincipal)
txtDireccion.grid(column=3, row=2, padx=3, pady=3)

btnGuardar = Button(ventanaProveedor, text="Guardar",command=guardarProveedor)
btnGuardar.grid(column=0,row=3, padx=3,pady=3, columnspan=2)

datos = ttk.Treeview(ventanaProveedor, height=10,  columns=("id_proveedor", "cedula", "nombres", "empresa", "correo", "direccion"), show="headings" )
datos.grid(column=0, row=4, padx=3, pady=3, columnspan=6)

datos.heading("id_proveedor", text="ID", anchor="center")
datos.column("id_proveedor", width=30)
datos.heading("cedula", text="CÉDULA", anchor="center")
datos.column("cedula", width=60)
datos.heading("nombres", text="NOMBRES Y APELLIDOS", anchor="center")
datos.column("nombres", width=150)
datos.heading("empresa", text="EMPRESA", anchor="center")
datos.column("empresa", width=150)
datos.heading("correo", text="CORREO", anchor="center")
datos.column("correo", width=150)
datos.heading("direccion", text="DIRECCIÓN", anchor="center")
datos.column("direccion", width=150)

cargarProveedor()

ventanaProveedor.mainloop()
