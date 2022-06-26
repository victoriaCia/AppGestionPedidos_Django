class Carro:
    def __init__(self,request):
        self.request=request      #almacena la peticion actual para poder utilizarla dps
        self.session=request.session     #inicia la sesion
        carro=self.session.get('carro')  #iguala la sesion con el carro
        if not carro:
            carro=self.session['carro']={}  #si no hay carro, lo creamos, el diccionario con prod en principio esta vacio
        
        self.carro=carro     #si se fue de la pag y dps vuelve, el carro es el q habia anteriormente

    def agregar_producto(self,producto):
        if (str(producto.id) not in self.carro.keys()):   #si el producto no esta en el carro
            self.carro[producto.id]={         #le asignamos como clave del producto, la clave del prod q agregamos recien
                "producto_id":producto.id,    # y como valor le asignamos otro diccionario con las prop del producto
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url,
            }
        else: 
            for key, value in self.carro.items():   #recorre el carro buscando el id de ese producto
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1   #en el valor de cantidad, le aumenta en 1
                    value["precio"]=float(value["precio"])+float(producto.precio)
                    break
        self.guardar_carro() #para q se actualize el carro y se guarde en la sesion

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True 

    def eliminar_producto(self,producto):
        producto.id=str(producto.id)   
        if producto.id in self.carro:    #si el producto esta en el carro
            del self.carro[producto.id]   #eliminar el producto del carro
            self.guardar_carro()

    def restar_producto(self,producto):
        for key, value in self.carro.items():
            if key==str(producto.id):
                value["cantidad"]=value["cantidad"]-1
                value["precio"]=float(value["precio"])-float(producto.precio)
                if value["cantidad"]<1:
                    self.eliminar_producto(producto)
                break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"]={}    #vuelve a contruir un diccionario vacio --> carro vacio
        self.session.modified=True




             