from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from api.models import  Proveedores
from api.schemas import  ProveedoresBase, ProveedoresOut, ProveedoresUpDate
from api.database import get_session 
router = APIRouter()

router = APIRouter()

#PROVEEDORES
@router.get("/proveedor/{id_proveedor}", response_model=ProveedoresBase)
def obtener_proveedor_por_id(id_proveedor: int, session: Session = Depends(get_session)):
    proveedor = session.get(Proveedores, id_proveedor)
    if not proveedor:
        raise HTTPException(status_code=404, detail="Proveedor no encontrado")
    return proveedor

@router.post("/proveedor/")
def crear_proveedor(proveedor:Proveedores, session:Session =Depends(get_session)):
    session.add(proveedor)
    session.commit()
    session.refresh(proveedor)
    return proveedor

@router.put("/proveedor/{id_proveedor}", response_model=ProveedoresOut)
def actualizar_proveedores(
    id_proveedor: int,
    proveedor: ProveedoresUpDate, 
    session: Session = Depends(get_session)
):
    proveedor_bd = session.get(id_proveedor)
    if not proveedor_bd:
        raise HTTPException(status_code=404, detail="proveedor no encontrado")

    proveedor_bd.Nombre = proveedor.Nombre
    proveedor_bd.Telefono = proveedor.Telefono
    proveedor_bd.Ciudad = proveedor.Ciudad
    proveedor_bd.Pais = proveedor.Pais
    
    session.add( proveedor_bd)
    session.commit()
    session.refresh( proveedor_bd)
    return  proveedor_bd
