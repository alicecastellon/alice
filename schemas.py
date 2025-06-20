from pydantic import BaseModel
from typing import Optional

#Clientes
class ClienteBase(BaseModel):
    Nombre: str
    Correo:str
    Direccion:str
    Telefono: Optional[int] = None
    

class ClienteOut(ClienteBase):
    id:int
    
    class Config:
        orm_mode = True
        
class ClienteUpdate(ClienteBase):
    Nombre: str | None = None
    Correo: str | None = None
    Direccion: str | None = None
    Telefono: Optional[int] = None
    
    
#Empleados
class EmpleadosBase(BaseModel):
    Primer_Nombre: str
    Primer_Apellido: str
    Identificacion: str
    Dirreccion: str
    Pais: str
    

class EmpleadosOut(EmpleadosBase):
    id_empleado: int
    
    class Config:
        orm_mode = True
        
class EmpleadosUpDate(EmpleadosBase):
    Primer_Nombre: str | None = None
    Primer_Apellido: str | None = None
    Identificacion: str | None = None
    Dirreccion_em: str | None = None
    Pais: str | None = None
    
#PROVEEDORES
class ProveedoresBase(BaseModel):
    Nombre:str
    Telefono: int
    Ciudad: str
    Pais: str
    
class ProveedoresOut(ProveedoresBase):
    id_proveedor: int
    
    class confing:
        orm_mode = True
        
class ProveedoresUpDate(ProveedoresOut):
    Nombre:str | None = None
    Telefono: int | None = None
    Ciudad: str | None = None
    Pais: str | None = None