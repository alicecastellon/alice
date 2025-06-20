from sqlmodel import SQLModel, Field

#Se esta creando la primera tabla llamada clientes con sus columnas
class Clientes(SQLModel, table=True):
    __tablename__='Clientes'
    id_cliente:int = Field(default=None, primary_key=True)
    Nombre:str =Field()
    Correo:str  =Field()
    Telefono: int = Field()
    Direccion:str  =Field()
    
    
#Se esta creando la segunda tabla llamada empleados con sus columnas
class Empleados(SQLModel, table=True):
    __tablename__= 'Empleados'
    id_empleado:int = Field(default=None, primary_key=True)
    Primer_Nombre:str = Field()
    Primer_Apellido:str = Field()
    Identificacion:str = Field()
    Direccion_em:str = Field()
    Pais:str = Field()
    

#Se esta creando la tercera tabla llamada proveedores con sus columnas
class Proveedores(SQLModel, table=True):
    __tablename__='Proveedores'
    id_proveedor:int = Field(default=None, primary_key=True)
    Nombre:str =Field()
    Telefono:int =Field()
    Ciudad:str =Field()
    Pais:str =Field()
  