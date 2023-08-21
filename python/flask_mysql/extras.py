class Producto:
    def __init__(self, product_id, product_name, model_year, brand_id, category_id, list_price):
        self.product_id = product_id
        self.product_name = product_name
        self.model_year = model_year
        self.brand_id = brand_id
        self.category_id = category_id
        self.list_price = list_price

class Marca:
    def __init__(self, brand_id, brand_name):
        self.brand_id = brand_id
        self.brand_name = brand_name

class Categoria:
    def __init__(self, category_id, category_name):
        self.category_id = category_id
        self.category_name = category_name

class Venta:
    def __init__(self, venta_id, product_id, sucursal_id, fecha_venta, quantity, total_venta, cantidad_productos):
        self.venta_id = venta_id
        self.product_id = product_id
        self.sucursal_id = sucursal_id
        self.fecha_venta = fecha_venta
        self.quantity = quantity
        self.total_venta = total_venta
        self.cantidad_productos = cantidad_productos
