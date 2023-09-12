from tkinter import *

ventanaProveedor = Tk()
ventanaProveedor.title("Adminitración de proveedores")
ventanaProveedor.geometry("600x600")

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

btnGuardar = Button(ventanaProveedor, text="Guardar")
btnGuardar.grid(column=0,row=3, padx=3,pady=3, columnspan=2)
ventanaProveedor.mainloop()
