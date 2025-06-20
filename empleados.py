from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from api.models import  Empleados
from api.schemas import  EmpleadosBase, EmpleadosOut, EmpleadosUpDate
from api.database import get_session 
router = APIRouter()

router = APIRouter()

@router.get("/empleado/{id_empleado}", response_model=EmpleadosBase)
def obtener_empleados_por_id(id_empleado: int, session: Session = Depends(get_session)):
    empleados = session.get(Empleados, id_empleado)
    if not empleados:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return empleados

@router.post("/empleado/")
def crear_empleados(empleado:Empleados, session:Session =Depends(get_session)):
    session.add(empleado)
    session.commit()
    session.refresh(empleado)
    return empleado

@router.put("/empleado/{id_empleado}", response_model=EmpleadosOut)
def actualizar_empleado(
    id_empleado: int,
    empleado: EmpleadosUpDate, 
    session: Session = Depends(get_session)
):
    empleado_bd = session.get(id_empleado)
    if not empleado_bd:
        raise HTTPException(status_code=404, detail="cliente no encontrado")

    empleado_bd.Primer_Nombre = empleado.Primer_Nombre
    empleado_bd.Primer_Apellido = empleado.Primer_Apellido 
    empleado_bd.Identificacion = empleado.Identificacion
    empleado_bd.Direccion_em = empleado.Direccion_em
    empleado_bd.Pais = empleado.Pais
    
    session.add( empleado_bd)
    session.commit()
    session.refresh( empleado_bd)
    return  empleado_bd
