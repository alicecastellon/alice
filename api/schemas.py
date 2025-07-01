from pydantic import BaseModel

#Clientes
class ClienteBase(BaseModel):
    nombre: str
    correo: str

class ClienteCreate(ClienteBase):
    pass

class ClienteOut(ClienteBase):
    id_usuario: int

    class Config:
        orm_mode = True


class ClienteUpdate(ClienteBase):
    nombre: str | None = None
    correo: str | None = None
    
#Empleados
class EmpleadosBase(BaseModel):
    Primer_Nombre: str
    Primer_Apellido: str
    Identificacion: str
    Direccion: str
    Pais: str
    

class EmpleadosOut(EmpleadosBase):
    id_empleado: int
    
    class Config:
        orm_mode = True
        
class EmpleadosUpDate(EmpleadosBase):
    Primer_Nombre: str | None = None
    Primer_Apellido: str | None = None
    Identificacion: str | None = None
    Direccion_em: str | None = None
    Pais: str | None = None
    
#PROVEEDORES
class ProveedoresBase(BaseModel):
    Nombre:str
    Telefono: int
    Ciudad: str
    Pais: str
    
class ProveedoresOut(ProveedoresBase):
    id_proveedor: int
    
    class config:
        orm_mode = True
        
class ProveedoresUpDate(ProveedoresOut):
    Nombre:str | None = None
    Telefono: int | None = None
    Ciudad: str | None = None
    Pais: str | None = None
    
    
#Producto

class ProductoBase(BaseModel):
    nombre: str
    correo: str

class ProductoCreate(ProductoBase):
    pass

class ProductoOut(ProductoBase):
    id_producto: int

    class Config:
        orm_mode = True


class ProductoUpdate(ProductoBase):
    nombre: str | None = None
    correo: str | None = None
    
#categotia
