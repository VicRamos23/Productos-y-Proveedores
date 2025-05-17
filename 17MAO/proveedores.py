class Proveedor:
    def __init__(self):
        self.apellidos = ""
        self.nombre = ""
        self.telefono = ""
        self.productos = []

    def agregar_proveedor(self, apellidos, nombre, telefono):
        self.apellidos = apellidos
        self.nombre = nombre
        self.telefono = telefono

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_datos(self):
        return f"{self.nombre} {self.apellidos} - Tel: {self.telefono}"

    def listar_productos(self):
        if not self.productos:
            return "   No hay productos registrados para este proveedor."
        salida = ""
        for idx, p in enumerate(self.productos, 1):
            salida += f"   {idx}. {p}\n"
        return salida.strip()
