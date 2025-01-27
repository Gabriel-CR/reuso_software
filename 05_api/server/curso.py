from pydantic import BaseModel

# Modelo para representar um curso
class Curso(BaseModel):
    id: int
    titulo: str
    descricao: str
    carga_horaria: int