from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import SQLModel
from .routes import router
from .database import engine

def create_app():
    app = FastAPI(
        title="Mi API de Farmacia", 
        description="Una API para gestionar toda informacion de la Farmacia",
        version="1.0.0",
    )
    
    
    
    SQLModel.metadata.create_all(bind=engine)

    origins = [
        "http://localhost",     
        "http://localhost:3000",  
        "http://localhost:8000",  
        "http://localhost:8080",
        "http://127.0.0.1:5500",  
        "http://127.0.0.1:5500",
        
    ]
    

    app.add_middleware(
        CORSMiddleware,            
        allow_origins=origins,     
        allow_credentials=True,    
        allow_methods=["*"],      
        allow_headers=["*"],     
    )
    app.include_router(router)
    return app