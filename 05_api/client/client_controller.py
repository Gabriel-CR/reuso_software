import requests

BASE_URL = "http://127.0.0.1:8000/cursos"

class ClientController:
  def __init__(self):
    pass

  def get_next_id(self):
    try:
      response = requests.get(BASE_URL)
      response.raise_for_status()
      cursos = response.json()
      return max((curso["id"] for curso in cursos), default=0) + 1
    except requests.exceptions.RequestException as e:
      print(f"Erro ao obter o próximo ID")
      return False

  def get_cursos(self):
    try:
      response = requests.get(BASE_URL)
      response.raise_for_status()
      cursos = response.json()
      return cursos
    except requests.exceptions.RequestException as e:
      print(f"Erro ao listar cursos")
      return False
    
  def get_curso(self, id):
    try:
      response = requests.get(f"{BASE_URL}/{id}")
      response.raise_for_status()
      curso = response.json()
      return curso
    except requests.exceptions.RequestException as e:
      print(f"Erro ao obter curso {id}")
      return False
    
  def post_curso(self, curso):
    try:
      response = requests.post(BASE_URL, json=curso)
      response.raise_for_status()
      return True
    except requests.exceptions.RequestException as e:
      print(f"Erro ao criar curso")
      return False
    
  def put_curso(self, id, curso):
    try:
      response = requests.put(f"{BASE_URL}/{id}", json=curso)
      response.raise_for_status()
      return True
    except requests.exceptions.RequestException as e:
      print(f"Erro ao atualizar curso {id}")
      return False
    
  def delete_curso(self, id):
    try:
      response = requests.delete(f"{BASE_URL}/{id}")
      response.raise_for_status()
      return True
    except requests.exceptions.RequestException as e:
      print(f"Erro ao excluir curso {id}")
      return False

  def listar_cursos(self):
    cursos = self.get_cursos()
    if cursos:
      for curso in cursos:
        print(f"ID: {curso['id']}, Título: {curso['titulo']}")
    else:
      print("Nenhum curso cadastrado.")

  def obter_curso(self):
    try:
      id = int(input("Digite o ID do curso: "))
    except ValueError:
      print("ID inválido. Operação cancelada.")
      return
    
    curso = self.get_curso(id)
    if curso:
      print(f"ID: {curso['id']}, Título: {curso['titulo']}, Descrição: {curso['descricao']}, Carga Horária: {curso['carga_horaria']}")
    else:
      print("Curso não encontrado.")

  def criar_curso(self):
    if not (novo_id := self.get_next_id()):
      return
    
    titulo = input("Digite o título do curso: ")
    descricao = input("Digite a descrição do curso: ")
    try:
      carga_horaria = input(f"Digite a carga horária do curso: ")
      carga_horaria = int(carga_horaria)
    except ValueError:
      print("Carga horária inválida. Operação cancelada.")
      return
    curso = {
      "id": novo_id,
      "titulo": titulo,
      "descricao": descricao,
      "carga_horaria": carga_horaria
    }

    if self.post_curso(curso):
      print(f"Curso criado com sucesso! ID gerado: {novo_id}")

  def atualizar_curso(self):
    try:
      id = int(input("Digite o ID do curso a ser atualizado: "))
    except ValueError:
      print("ID inválido. Operação cancelada.")
      return
    
    curso = self.get_curso(id)
    if not curso:
      print("Curso não encontrado.")
      return

    titulo = input(f"Digite o novo título do curso (atual: {curso['titulo']}): ") or curso["titulo"]
    descricao = input(f"Digite a nova descrição do curso (atual: {curso['descricao']}): ") or curso["descricao"]
    try:
      carga_horaria = input(f"Digite a nova carga horária do curso (atual: {curso['carga_horaria']}): ")
      carga_horaria = int(carga_horaria) if carga_horaria else curso["carga_horaria"]
    except ValueError:
      print("Carga horária inválida. Operação cancelada.")
      return

    curso_atualizado = {
      "id": id,
      "titulo": titulo,
      "descricao": descricao,
      "carga_horaria": carga_horaria
    }

    if self.put_curso(id, curso_atualizado):
      print("Curso atualizado com sucesso!")

  def excluir_curso(self):
    try:
      id = int(input("Digite o ID do curso a ser excluído: "))
    except ValueError:
      print("ID inválido. Operação cancelada.")
      return
    
    if self.delete_curso(id):
      print("Curso excluído com sucesso!")