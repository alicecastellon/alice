from sqlmodel import SQLModel, Field
from typing import Optional

#Se esta creando la primera tabla llamada clientes con sus columnas
class Cliente(SQLModel, table=True):
    id_usuario: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    correo: str
    
    
#Se esta creando la segunda tabla llamada empleados con sus columnas
class Empleados(SQLModel, table=True):
    __tablename__= 'Empleados'
    id_empleado:int = Field(default=None, primary_key=True)
    primer_nombre:str 
    primer_apellido:str 
    identificacion:str 
    direccion_em:str 
    pais:str 
    

#Se esta creando la tercera tabla llamada proveedores con sus columnas
class Proveedores(SQLModel, table=True):
    __tablename__='Proveedores'
    id_proveedor:int = Field(default=None, primary_key=True)
    nombre:str 
    telefono:int 
    ciudad:str 
    pais:str 
    
#Se esta creando la cuarta tabla llamada producto con sus columnas 
class Productos(SQLModel, table=True):
    __tablename__= 'Productos'
    id_producto: int = Field(default=None, primary_key=True)
    nombre_producto: str
    precio: str 
    
    
