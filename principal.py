from tkinter import *
from tkinter import ttk
from conexionMysql import conexion

ventanaPrinpal = Tk()
ventanaPrinpal.geometry("1200x800")
ventanaPrinpal.title("Ventana Principal")
#Función para cargar datos del proveedor
def cargarProveedor():
    sql = "SELECT * FROM proveedores"
    return conexion.ejecutar(sql,())
#función para la construcción de una ventana hija
def ventaHijaProductos():
    ventanaProductos =Toplevel(ventanaPrinpal)
    ventanaProductos.title("Administación de productos") 
    ventanaProductos.geometry("500x300")

    Label(ventanaProductos, text="Nombre:").grid(column=0, row=0, padx=3, pady=3)
    txtNombre = Entry(ventanaProductos)
    txtNombre.grid(column=1, row=0, padx=3, pady=3)

    Label(ventanaProductos, text="Precio:").grid(column=2, row=0, padx=3, pady=3)
    txtPrecio = Entry(ventanaProductos)
    txtPrecio.grid(column=3, row=0, padx=3, pady=3)

    Label(ventanaProductos, text="stock:").grid(column=0, row=1, padx=3, pady=3)
    txtStock = Entry(ventanaProductos)
    txtStock.grid(column=1, row=1, padx=3, pady=3)

    Label(ventanaProductos, text="Proveedor:").grid(column=2, row=1, padx=3, pady=3)
    cbxProvedor = ttk.Combobox(ventanaProductos)
    cbxProvedor.grid(column=3, row=1, padx=3, pady=3)
    data = cargarProveedor()
    cache = list()
    cbxProvedor.insert(0,"Seleccione un proveedor")
    for row in data:
        cache.append(row[2]) 
    cbxProvedor["values"] = cache

Button(ventanaPrinpal, text="Ventan Producto", command=ventaHijaProductos).pack() 
ventanaPrinpal.mainloop()