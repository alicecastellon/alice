from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from api.models import Clientes
from api.schemas import  ClienteOut, ClienteUpdate, ClienteBase
from api.database import get_session 
router = APIRouter()

router = APIRouter()

@router.get("/cliente/{id}", response_model=ClienteBase)
def obtener_clinete_por_id(id: int, session: Session = Depends(get_session)):
    Cliente = session.get(Clientes, id)
    if not Cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return Cliente

@router.post("/Cliente/")
def crear_cliente(cliente:Clientes, session:Session =Depends(get_session)):
    session.add(cliente)
    session.commit()
    session.refresh(cliente)
    return cliente


@router.put("/cliente/{id}", response_model=ClienteOut)
def actualizar_cliente(
    id: int,
    cliente: ClienteUpdate, 
    session: Session = Depends(get_session)
):
    cliente_bd = session.get( id)
    if not cliente_bd:
        raise HTTPException(status_code=404, detail="cliente no encontrado")

    cliente_bd.Nombre = cliente.Nombre
    cliente_bd.Correo = cliente.Correo 
    cliente_bd.Direccion = cliente.Direccion 
    cliente_bd.Telefono = cliente.Telefono 

    session.add(cliente_bd)
    session.commit()
    session.refresh(cliente_bd)
    return cliente_bd
