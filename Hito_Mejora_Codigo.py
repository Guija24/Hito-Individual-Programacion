
class Cliente:
    def __init__(self,id,nombre,apellidos,ciudad,email,telf):
        self.id=id 
        self.nombre=nombre 
        self.apellidos=apellidos
        self.ciudad=ciudad
        self.email=email
        self.telf=telf
    def Info_Cliente(self):
        print(f'El cliente se llama {self.nombre} {self.apellidos} , su email es: {self.email} y su telf es: {self.telf} y reside en:{self.ciudad}')

class Producto:
    def __init__(self,id_producto,nombre_producto,unidades,precio):
        self.id_producto=id_producto
        self.nombre_producto=nombre_producto
        self.unidades=unidades
        self.precio=precio 
    def Info_Product(self):
        print(f'Los datos del producto son {self.nombre_producto} y cuesta: {self.precio}€')


class Pedidos:
    def __init__(self,id_factura,fecha_factura,cliente,producto):
        self.id_factura=id_factura
        self.fecha=fecha_factura
        self.cliente=cliente 
        self.producto=producto

    def Info_Pedido(self):
        print(f'Detalles de pedido {self.id_factura} - {self.fecha}  - {self.cliente} - {self.producto}')

    def Add_Deseos(self):
        print('El producto a sido añadido a la lista de deseos')

    def End_Shop(self):
        print('Compra realizada con exito')

    def Pago(self):
        print('Pago realizado con tarjeta: XXXX XXXX XXXX 2509')

    def Fact_Pdf(self):
        print('La factura a sido enviada en PDF')

    def Seguimiento(self):
        print('SMS enviado al cliente con exito')


Cliente1=Cliente(254,'Ivan', 'Guijarro Soto','Madrid','ivan.guijarro@campusfp.es',602254587)
Producto1=Producto(589,'Coche',2588,12350)
Pedido1=Pedidos(124,14_12_2022,'Ivan','Coche')

print()
Cliente1.Info_Cliente()
print()
Producto1.Info_Product()
print()
Pedido1.Info_Pedido()
print()
Pedido1.Add_Deseos()
print()
Pedido1.End_Shop()
print()
Pedido1.Pago()
print()
Pedido1.Fact_Pdf()
print()
Pedido1.Seguimiento()
print()

