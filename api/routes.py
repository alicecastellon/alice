from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from api.models import Cliente, Empleados, Proveedores, Productos
from api.schemas import   ClienteUpdate, EmpleadosUpDate, ProveedoresUpDate

from api.database import get_session 
router = APIRouter()

router = APIRouter()

#CLIENTES


@router.get("/clientes/")
def obtener_cliente(session:Session = Depends(get_session)):
    statement = select(Cliente)
    cliente = session.exec(statement).all()
    return cliente

@router.put("/clientes/{id_cliente}",response_model=Cliente)
def actualizar_cliente(id_cliente : int, datos: ClienteUpdate, session = Depends(get_session)):
    cliente = session.get(Cliente, id_cliente)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")

@router.post("/clientes/")
def crear_cliente(cliente: Cliente, session:Session = Depends(get_session)):
    session.add(cliente)
    session.commit()
    session.refresh(cliente)
    return cliente

@router.delete("/clientes/")
def eliminar_cliente(id_cliente: int, session:Session = Depends(get_session)):
    cliente = session.get (Cliente, id_cliente)
    if not cliente:
        raise HTTPException(status_code=404, detail="cliente no encontrado")
    session.delete(cliente)
    session.commit()
    return None



#EMPLEADOS

@router.get("/empleados/")
def obtener_empleados(session:Session = Depends(get_session)):
    statement = select(Empleados)
    empleado = session.exec(statement).all()
    return empleado

@router.put("/empleados/{id_empleado}",response_model=Empleados)
def actualizar_empleado(id_empleado : int, datos: EmpleadosUpDate, session = Depends(get_session)):
    empleado = session.get(Empleados,id_empleado)
    if not empleado:
        raise HTTPException(status_code=404, detail="empleado no encontrado")

@router.post("/Empleado/")
def crear_empleado(empleado: Empleados, session:Session = Depends(get_session)):
    session.add(empleado)
    session.commit()
    session.refresh(empleado)
    return empleado

@router.delete("/empleado/")
def eliminar_empleado(id_empleado: int, session:Session = Depends(get_session)):
    empleado = session.get (Empleados, id_empleado)
    if not empleado:
        raise HTTPException(status_code=404, detail="empleado no encontrado")
    session.delete(empleado)
    session.commit()
    return None

#PROVEEDORES

@router.get("/proveedores/")
def obtener_proveedores(session:Session = Depends(get_session)):
    statement = select(Proveedores)
    proveedores = session.exec(statement).all()
    return proveedores

@router.put("/proveedores/{id_proveedor}",response_model=Proveedores)
def actualizar_proveedores(id_proveedor : int, datos: ProveedoresUpDate, session = Depends(get_session)):
    proveedores = session.get(Proveedores,id_proveedor)
    if not proveedores:
        raise HTTPException(status_code=404, detail="Proveedores no encontrado")

@router.post("/proveedores/")
def crear_proveedor(proveedores: Proveedores, session:Session = Depends(get_session)):
    session.add(proveedores)
    session.commit()
    session.refresh(proveedores)
    return proveedores

@router.delete("/proveedores/")
def eliminar_proveedores(id_proveedores: int, session:Session = Depends(get_session)):
    proveedores = session.get (Proveedores,id_proveedores)
    if not proveedores:
        raise HTTPException(status_code=404, detail="proveedores no encontrado")
    session.delete(proveedores)
    session.commit()
    return None

#producto

@router.get("/productos/")
def obtener_productos(session:Session = Depends(get_session)):
    statement = select(Productos)
    productos = session.exec(statement).all()
    return productos

@router.put("/productos/{id_producto}",response_model=Productos)
def actualizar_productos(id_producto : int, datos: ProveedoresUpDate, session = Depends(get_session)):
    productos = session.get(Productos,id_producto)
    if not productos:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

@router.post("/productos/")
def crear_productos(productos: Productos, session:Session = Depends(get_session)):
    session.add(productos)
    session.commit()
    session.refresh(productos)
    return productos

@router.delete("/productos/")
def eliminar_productos(id_producto: int, session:Session = Depends(get_session)):
    productos = session.get (Productos,id_producto)
    if not productos:
        raise HTTPException(status_code=404, detail="productos no encontrado")
    session.delete(productos)
    session.commit()
    return None