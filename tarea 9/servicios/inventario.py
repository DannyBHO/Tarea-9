from modelo.producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []  # Lista principal de almacenamiento

    def añadir_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("⚠️ Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print("✅ Producto añadido con éxito.")

    def eliminar_producto(self, id):
        for p in self.productos:
            if p.get_id() == id:
                self.productos.remove(p)
                print("🗑️ Producto eliminado con éxito.")
                return
        print("⚠️ Producto no encontrado.")

    def actualizar_producto(self, id, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("🔄 Producto actualizado con éxito.")
                return
        print("⚠️ Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = []
        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                encontrados.append(p)

        if encontrados:
            print("\n🔎 Resultados de búsqueda:")
            for p in encontrados:
                print(p)
        else:
            print("⚠️ No se encontraron productos con ese nombre.")

    def mostrar_inventario(self):
        if not self.productos:
            print("\n📦 El inventario está vacío.")
            return

        print("\n📦 INVENTARIO COMPLETO:")
        for p in self.productos:
            print(p)
