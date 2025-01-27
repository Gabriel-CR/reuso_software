from fastapi import FastAPI, HTTPException
from typing import List
from curso import Curso

app = FastAPI()

# Banco de dados em memória
cursos_db = []

@app.get("/cursos", response_model=List[Curso])
def listar_cursos():
    """Retorna todos os cursos disponíveis."""
    return cursos_db

@app.get("/cursos/{id}", response_model=Curso)
def obter_curso(id: int):
    """Retorna os detalhes de um curso específico pelo ID."""
    for curso in cursos_db:
        if curso.id == id:
            return curso
    raise HTTPException(status_code=404, detail="Curso não encontrado")

@app.post("/cursos", response_model=Curso)
def criar_curso(curso: Curso):
    """Adiciona um novo curso."""
    if any(c.id == curso.id for c in cursos_db):
        raise HTTPException(status_code=400, detail="ID do curso já existe")
    cursos_db.append(curso)
    return curso

@app.put("/cursos/{id}", response_model=Curso)
def atualizar_curso(id: int, curso_atualizado: Curso):
    """Atualiza as informações de um curso existente."""
    for index, curso in enumerate(cursos_db):
        if curso.id == id:
            cursos_db[index] = curso_atualizado
            return curso_atualizado
    raise HTTPException(status_code=404, detail="Curso não encontrado")

@app.delete("/cursos/{id}", response_model=dict)
def excluir_curso(id: int):
    """Remove um curso pelo ID."""
    for index, curso in enumerate(cursos_db):
        if curso.id == id:
            del cursos_db[index]
            return {"message": "Curso excluído com sucesso"}
    raise HTTPException(status_code=404, detail="Curso não encontrado")
